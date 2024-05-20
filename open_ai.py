from openai import OpenAI

def get_promt(api_key , promt , text):
    client = OpenAI(api_key=f"{api_key}", base_url="https://api.deepseek.com/v1")

    response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": f'{promt}'},
        {"role": "user", "content": f'{text}'},
    ]
    )
    return response.choices[0].message.content