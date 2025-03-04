from openai import OpenAI

# Define a function to generate text based on the provided prompt
def generate_text(prompt_type: str, story_poem_prompt: str, api_key: str) -> str:
    """
    Generate a story or poem based on the user input

    Args: 
        - prompt_type (str): The type of text to generate (story or poem)
        - story_poem_prompt (str): The prompt to use for generating the text
        - api_key (str): The API key for authenticating with OpenAI

    Returns:
        - str: The generated story or poem
    """ 

    client = OpenAI(api_key=api_key)

    # use the chat completion
    text_response = client.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = [
            {"role": "system", "content": f"You are a creative {prompt_type.lower()} writter"},
            {"role": "user", "content": f"Write a {prompt_type.lower()} based on the following prompt: {story_poem_prompt}"}
        ]
    )

    # return the generated text
    return text_response.choices[0].message.content.strip()