import json
from logging import getLogger

import requests
from config import cast_config

logger = getLogger(__name__)

TTS_API = "tts"


class TTSClient:
    base_url: str
    tts_url: str

    def __init__(self, base_url: str) -> None:
        self.base_url = base_url
        self.tts_url = f"{self.base_url}/{TTS_API}"

    def call_server(self, prompt: str, voice: str = "v2/en_speaker_9") -> requests.Response:
        """
        Calls the TTS server with the given prompt and voice.

        Args:
            prompt (str): Prompt to generate speech for.
            voice (str): Voice to use for speech generation.

        Returns:
            requests.Response: Response from the TTS server.
        """
        payload = json.dumps({"prompt": prompt, "voice": voice})
        headers = {"Content-Type": "application/json"}
        response = requests.request("GET", self.tts_url, headers=headers, data=payload)
        return response


def generate_podcast(script: str) -> bytes:
    """
    Generates a podcast from the given script using the TTS client.

    Args:
        script (str): Script to generate the podcast from.

    Returns:
        bytes: Podcast audio.
    """
    logger.info(f"Generating podcast from script: {script}")
    client = TTSClient(cast_config.tts_base_url)
    resp = client.call_server(script)
    return resp.content
