import logging

import scipy
import torch
from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
from transformers import BarkModel, BarkProcessor

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class TextRequest(BaseModel):
    prompt: str
    voice: str = "v2/en_speaker_9"


app = FastAPI()


@app.get("/tts", response_class=FileResponse)
async def text_to_speech(request: TextRequest):
    """
    Generates an audio file based on the provided text prompt and voice preset.

    Args:
        request (TextRequest): Pydantic model containing the text prompt and voice preset.

    Returns:
        FileResponse: FastAPI response object containing the generated audio file.
    """
    # load the model using the pipeline method
    model = BarkModel.from_pretrained("suno/bark-small")

    # check if gpu is available
    device = "cuda:0" if torch.cuda.is_available() else "cpu"
    model = model.to(device)
    logger.info(f"Using device: {device} to run the model: {model.name_or_path}")

    processor = BarkProcessor.from_pretrained("suno/bark-small", torch_dtype=torch.float16)

    # prepare the inputs
    text_prompt = request.prompt
    voice_preset = request.voice
    logger.info(f"Using voice: {voice_preset} to process text prompt: {text_prompt}")
    inputs = processor(text_prompt, voice_preset=voice_preset)

    # generate speech
    speech_output = model.generate(**inputs.to(device))
    logger.info(f"Generated speech output {speech_output}")

    # save to a wav file
    sampling_rate = model.generation_config.sample_rate
    scipy.io.wavfile.write("bark_out.wav", rate=sampling_rate, data=speech_output[0].cpu().numpy())

    # return the audio file as a response
    return FileResponse("bark_out.wav")
