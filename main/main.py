import openai

openai.api_key = ''

audio_file = open("audio.mp4", "rb")
transcript = openai.Audio.transcribe("whisper-1", audio_file).text

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You will do a resume of the music"},
    {"role": "user", "content": f"{transcript}"}
  ]
)

print("***************************MUSIC********************************")
print(completion.choices[0].message.content)
print("****************************************************************")