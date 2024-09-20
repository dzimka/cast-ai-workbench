import os

from langchain_ollama import OllamaEmbeddings, OllamaLLM


class CastConfig:
    llm_model: str
    llm_base_url: str
    tts_model: str
    tts_base_url: str
    data_path: str

    def __init__(self, **kwargs):
        self.llm_base_url = kwargs.get("llm_base_url", "http://jetson-nano:11434")
        self.llm_model = kwargs.get("llm_model", "mistral")
        self.tts_base_url = kwargs["tts_base_url", "http://jetson-nano:8000"]
        self.data_path = kwargs["data_path"]

    def get_llm(self) -> OllamaLLM:
        """
        Returns an instance of the OllamaLLM class, which is used to interact with the LLM model.

        Returns:
            OllamaLLM: An instance of the OllamaLLM class.
        """
        return OllamaLLM(base_url=self.llm_base_url, model=self.llm_model)

    def get_llm_embed(self) -> OllamaEmbeddings:
        """
        Returns an instance of the OllamaEmbeddings class, which is used to interact with the LLM model
        for embedding purposes.

        Returns:
            OllamaEmbeddings: An instance of the OllamaEmbeddings class.
        """
        return OllamaEmbeddings(base_url=self.llm_base_url, model=self.llm_model)


params = {
    "llm_base_url": os.environ.get("CAST_AI_LLM_BASE_URL"),
    "llm_model": os.environ.get("CAST_AI_LLM_MODEL"),
    "tts_base_url": os.environ.get("CAST_AI_TTS_BASE_URL"),
    "data_path": os.environ.get("CAST_AI_DATA_PATH"),
}

# create a single instance of the app configuration
cast_config = CastConfig(**params)
