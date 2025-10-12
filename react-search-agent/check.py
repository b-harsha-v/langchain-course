import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load your API key from the .env file
load_dotenv()
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

# Loop through and print the available models
print("Available Models:")
for model in genai.list_models():
  # We check if the model supports the 'generateContent' method
  if 'generateContent' in model.supported_generation_methods:
    print(f"- {model.name}")