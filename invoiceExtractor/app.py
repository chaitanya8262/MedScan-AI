## Invoice Extractor

from dotenv import load_dotenv  # to load .env api key

load_dotenv() ## load all environmental variables

import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

## configure api key

genai.configure(api_key = os.getenv("API_KEY"))

## function to load Gemini Pro vision model and get response

def get_gemini_response(input, image, prompt):
    model = genai.GenerativeModel("gemini-pro-vision")
    response = model.generate_content([input, image[0], prompt])
    return response.text

def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        #read the file into bytes
        bytes_data = uploaded_file.getvalue()

        image_parts = [{
            "mime_type": uploaded_file.type, #Get the MIME type of the uploaded file
            "data": bytes_data,
        }]
        return image_parts
    else:
        raise FileNotFoundError("No file was uploaded")

## Intialize our Streamlit app

st.set_page_config(page_title="Gemini image-Invoice Extractor")

st.header("Gemini application")
input=st.text_input("Input Prompt: ", key="input")
uploaded_file =st.file_uploader("Upload an image..", type=["png", "jpg", "jpeg"])
image=""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)


submit = st.button("Tell me about the invoice")

input_prompts ="""
You are expert in undersanding invoices. You will recieve input 
as invoices and you will have to answer
questions based on the input image """

## if submit button is clicked

if submit:
    image_data = input_image_setup(uploaded_file)
    response=get_gemini_response(input_prompts, image_data,input)

    st.subheader("The Response is")
    st.write(response)