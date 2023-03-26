import os
import openai

openai.api_key = 'my_api_key'

openai.Image.create(
  prompt="A cute baby sea otter",
  n=2,
  size="1024x1024"
)
