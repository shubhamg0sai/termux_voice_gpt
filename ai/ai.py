import openai
from apikey import api_data

prompt = " "

def ai(query):
    openai.api_key = api_data
    global prompt
    prompt=f'sir: {query}\n '
    print(prompt)
    response=openai.Completion.create(
        model="text-davinci-003",
        prompt= prompt,
        temperature=0.9,
        max_tokens=4000,
        n=1,
        stop=None,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    words=response.choices[0].text.strip()
    answer=words
    prompt += f"{response['choices'][0]['text']}\n"
    return answer
