from modules.user_interface import gradio_interface


if __name__ == "__main__":
    demo = gradio_interface()
    demo.launch(share=True)