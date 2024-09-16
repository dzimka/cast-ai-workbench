import os

from langchain_ollama import OllamaEmbeddings, OllamaLLM


class CastConfig:
    llm_model: str
    llm_base_url: str
    tts_model: str
    tts_base_url: str
    data_path: str

    def __init__(self, **kwargs) -> None:
        self.llm_base_url = kwargs["llm_base_url"] if "llm_base_url" in kwargs else "http://jetson-nano:11434"
        self.llm_model = kwargs["llm_model"] if "llm_model" in kwargs else "mistral"
        self.tts_base_url = kwargs["tts_base_url"]
        self.data_path = kwargs["data_path"]

    def get_llm(self) -> OllamaLLM:
        return OllamaLLM(base_url=self.llm_base_url, model=self.llm_model)

    def get_llm_embed(self) -> OllamaEmbeddings:
        return OllamaEmbeddings(base_url=self.llm_base_url, model=self.llm_model)


params = {
    "llm_base_url": os.environ.get("CAST_AI_LLM_BASE_URL"),
    "llm_model": os.environ.get("CAST_AI_LLM_MODEL"),
    "tts_base_url": os.environ.get("CAST_AI_TTS_BASE_URL"),
    "data_path": os.environ.get("CAST_AI_DATA_PATH"),
}

cast_config = CastConfig(**params)
