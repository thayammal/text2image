from PIL import Image
import io
import requests
import streamlit as st

API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
headers = {"Authorization": "Bearer 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"}

st.title("Text to Image Generator")


def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.content


prompt = st.text_input("Enter your prompt")
button_prompt = st.button("Generate Image")
if button_prompt:
    image_bytes = query({
        "inputs": prompt,
    })
# You can access the image with PIL.Image for example
    images = Image.open(io.BytesIO(image_bytes))
    st.image(images)
