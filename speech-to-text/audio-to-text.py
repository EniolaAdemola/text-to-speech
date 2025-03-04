import gradio as gr
from openai import OpenAI

def transcribe_audio(audio, api_key):
    """
    Transcribe the provided audio file to text using the OpenAI API's Whisper model.
    
    Parameter:
    - audio (str): The path to the audio file to transcribe.
    - api_key (str): The API key for authenticating with OpenAI.

    Returns:
    - str: The transcribed text.
    """
    
   # check if the API key was provided, if not
    if not api_key:
        raise gr.Error("Please enter your OpenAi API key")
    
    client = OpenAI(api_key=api_key)

    with open(audio, "rb") as audio_file:
        # transcribe the audio file using the Whisper model
        transcription = client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file
        )
    
    # return the transcribed text
    return transcription.text


def gradio_interface():
    """
      Create and launch a Gradio interface for the speech-to-text application
    """

    with gr.Blocks() as demo:
        gr.Markdown("# <center>OpenAI Speech to Text</center>")

        # create a row to display the input fields for OpenAI API key
        with gr.Row():
            api_key_input = gr.Textbox(label="OpenAI API Key", type="password", placeholder="Enter your OpenAI API key")

        # create an audio input field to upload the audio file
        audio_input = gr.Audio(sources="upload", type="filepath", label="Upload Audio File")

        transcribe_button = gr.Button("Transcribe")

        # create a textbox to display the transcribed text       
        transcription_output = gr.Textbox(label="Transcription", lines=10)


        # handle when the button is clicked
        transcribe_button.click(
            fn = transcribe_audio,
            inputs = [audio_input, api_key_input],
            outputs = transcription_output
        )

    demo.launch(share=True)


if __name__ == "__main__":
    gradio_interface()