import os
import openai

openai.api_key = 'my_api_key'

audio_file = open("audio.mp3", "rb")
transcript = openai.Audio.transcribe("whisper-1", audio_file)

print(transcript.text)