import requests

api_key =  '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'
endpoint = 'https://api.openai.com/v1/completions'

search = input('Pergunta: ')
model = 'text-davinci-003'

data = {
    'prompt': search,
    'model': model,
    'temperature': 0,
    'max_tokens': 2048    
}

response = requests.post(endpoint, json=data, headers={
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {api_key}'
})

if response.ok:
    resposta = response.json()['choices'][0]['text']
    print(resposta)
else:
    print(f"Erro na solicitação: {response.text}")