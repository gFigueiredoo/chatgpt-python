import os
import openai

openai.api_key = 'my-api-key'

prompt = input('Pergunta: ')

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {
        "role": "user", 
        "content": prompt
    }
  ]
)

print(completion.choices[0].message.content)
