import tempfile
from openai import OpenAI


def generate_speech(text: str, api_key: str, voice: str, tts_model: str) -> str:
    """
    Converts text into speech using OpenAI's TTS.

    Args:
        text (str): The text to convert.
        api_key (str): OpenAI API key.
        voice (str): Selected voice (e.g., "alloy", "fable").
        tts_model (str): Selected TTS model (e.g., "tts-1", "tts-1-hd").

    Returns:
        str: Path to the generated audio file.
    """
     
    client = OpenAI(api_key=api_key)

    speech_response = client.audio.speech.create(
         model=tts_model,
         voice=voice,
         input=text
    )

    #  save to a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_file:
        temp_file.write(speech_response.content)
        return temp_file.name