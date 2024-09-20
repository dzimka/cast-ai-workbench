import logging
import os

import gradio as gr
from config import cast_config
from llm_pipeline import generate_script, load_documents
from tts_pipeline import generate_podcast

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)
logger.info("Starting the application")


def create_script(topics: str):
    """
    Creates a script based on the given topics of interest.

    This function loads documents from a predefined data path and generates
    a script using the provided topics.

    Args:
        topics (str): A string containing the topics of interest.

    Returns:
        str: The generated script based on the input topics.
    """
    fragments = load_documents(cast_config.data_path)
    return generate_script(topics, fragments)


def create_podcast(script: str):
    """
    Creates an audio podcast based on the given script.

    This function generates an audio podcast using the provided script.

    Args:
        script (str): The script to be used for generating the podcast.

    Returns:
        str: The path to the generated audio podcast.
    """
    return generate_podcast(script)


with gr.Blocks(analytics_enabled=False) as demo:
    topics_input = gr.Text(value="Django", label="Topics of interest")
    generate_script_button = gr.Button("Generate Script")
    script_output = gr.Textbox(label="Generated script")
    generate_podcast_button = gr.Button("Generate Podcast")
    podcast_output = gr.Audio("Generated podcast")
    generate_script_button.click(create_script, inputs=topics_input, outputs=script_output)
    generate_podcast_button.click(create_podcast, inputs=script_output, outputs=podcast_output)


proxy_prefix = os.environ.get("PROXY_PREFIX")
demo.launch(server_name="0.0.0.0", server_port=8080, root_path=proxy_prefix)
