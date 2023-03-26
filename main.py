import openai

# Define a chave da API OpenAI
openai.api_key = "my-api-key"


# Define o prompt de entrada
prompt = input('Pergunta: ')

# Define as configurações de solicitação
completion = openai.Completion.create(
    prompt=prompt,
    max_tokens=1000,
    model="text-davinci-003"
)

# Imprime a resposta do modelo
print(completion.choices[0].text)
