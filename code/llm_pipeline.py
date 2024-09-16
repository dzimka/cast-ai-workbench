from logging import getLogger
from pathlib import Path
from typing import List

from config import cast_config
from langchain_chroma import Chroma
from langchain_community.document_loaders import TextLoader
from langchain_core.documents import Document
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_text_splitters import MarkdownHeaderTextSplitter

logger = getLogger(__name__)

PROMPT_TEMPLATE = """Use the following pieces of context to generate the podcast script tailored
to the topics asked in the question.
First select the most relevant context fragments.
Do not include the context that is not relevant to the question.
Do not add any new information, only use the provided context.
Then compile a list of segments that will be included in the podcast and generate the script for each segment.
Limit each segment to 5 sentences. Be nice and helpful to the listener.

{context}

Question: {question}
"""


def load_documents(path: str) -> List[Document]:
    file_paths = [str(file) for file in Path(path).iterdir()]
    logger.info(f"Detected {len(file_paths)} files in the path: {path}")
    splitter = MarkdownHeaderTextSplitter(headers_to_split_on=[("#", "Header 1")])
    fragments = []
    for file_path in file_paths:
        loader = TextLoader(file_path)
        docs = loader.load()
        fragments.extend(splitter.split_text(docs[0].page_content))  # TODO: iterate over all docs
    logger.info(f"Extracted {len(fragments)} fragments")
    return fragments


def format_docs(docs: List[Document]):
    return "\n\n".join(doc.page_content for doc in docs)


def generate_script(topics: str, fragments: List[Document]) -> str:
    vectorstore = Chroma.from_documents(documents=fragments, embedding=cast_config.get_llm_embed())
    retriever = vectorstore.as_retriever()
    custom_rag_prompt = PromptTemplate.from_template(PROMPT_TEMPLATE)
    logger.info("Running the LLM pipeline")
    rag_chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | custom_rag_prompt
        | cast_config.get_llm()
        | StrOutputParser()
    )
    return rag_chain.invoke(topics)
