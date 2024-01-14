import openai
from apikey import api_data

prompt = " "

def ai(query):
    openai.api_key = api_data
    global prompt
    prompt=f'sir: {query}\n '
    print(prompt)
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt }
            ]
        )
    words=response['choices'][0]['message']['content']
    answer=words
    prompt += f"{response['choices'][0]['text']}\n"
    return answer
