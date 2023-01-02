import os
import openai

openai.organization = "org-547KC0rnKSUBHnVItpy5Z1kf" 
key_os = os.environ["OPENAI_API_KEY"] 
openai.api_key=key_os
def get_model_list(): 
    return openai.Model.list()


def get_answer(question: str, model: str = "text-davinci-003"): 
    response = openai.Completion.create(
        model=model,
        prompt=question,
        temperature=0.5,
        max_tokens=1024,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    return response


def get_code(question: str, model: str = "code-davinci-002"): 
    response = openai.Completion.create(
        model=model,
        prompt=question,
        temperature=0,
        max_tokens=1024,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    return response
