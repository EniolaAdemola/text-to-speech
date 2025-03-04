import gradio as gr
from modules.generate_story_poem import generate_text
from modules.text_to_speech import generate_speech

def generate_content(prompt_type, story_poem_prompt, api_key, voice, tts_model):
    # Generate text and convert it to Adio
    if not api_key:
        raise gr.Error("Please enter your OpenAi API key")
    
    text = generate_text(prompt_type, story_poem_prompt, api_key)

    audio_file = generate_speech(text, api_key, voice, tts_model)

    return text, audio_file

def gradio_interface():
    """Generte the Gradio interface for the application"""

    with gr.Blocks() as demo:
        gr.Markdown("## Story/Poem Generator with Audio Output")

        # Create the input interface
        with gr.Row():
            prompt_type = gr.Dropdown(["Story", "Poem"], label="Prompt Type", value="Story")

            story_poem_prompt = gr.Textbox(lines=3, label="Story/Poem Prompt")

            api_key = gr.Textbox(label="OpenAI API Key", type="password")


        with gr.Row():
            voice = gr.Dropdown(["alloy", "echo", "fable", "onyx", "nova"], label="Voice", value="alloy")

            tts_model = gr.Dropdown(["tts-1", "tts-1-hd"], label="TTS Model", value="tts-1")

        generate_btn = gr.Button(f"Generate {prompt_type.value}")

        # Create the output interface
        with gr.Row():
            text_output = gr.Textbox(lines=10, label="Generated Text", interactive=False)

            audio_output = gr.Audio(label="Generated Audio", interactive=False)

        # Set the function to be called when the button is clicked
        generate_btn.click(
            fn = generate_content,
            inputs = [prompt_type, story_poem_prompt, api_key, voice, tts_model],
            outputs = [text_output, audio_output]
        )

    return demo

