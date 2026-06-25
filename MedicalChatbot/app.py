import streamlit as st
from pathlib import Path
import google.generativeai as genai

from api_key import api_key

#configure genai with api_key
genai.configure(api_key=api_key)

#set up the model
generation_config = {
    "temperature": 0.4,
    "top_p": 1,
    "top_k": 32,
    "max_output_tokens": 4096
}
 
#apply safety settings
safefy_settings = {
     "HARM_CATEGORY_HARASSMENT": "BLOCK_NONE",
    "HARM_CATEGORY_HATE_SPEECH": "BLOCK_NONE",
    "HARM_CATEGORY_SEXUALLY_EXPLICIT": "BLOCK_NONE",
    "HARM_CATEGORY_DANGEROUS_CONTENT": "BLOCK_NONE",

}

system_prompts=""" 
As a highly skilled medical practitioner specializing in image analysis, you are tasked with examining medical images for a reowned hospital. Your expertise in crucial  in identifying any diseases, or health issues that may be present in the image.

Your Responsibilities include:

1. Detailed Analysis: Throughly analyze each image, focusing on identifying any abnormal findings.
2. Findings Report: Document all observed anomalies in a detailed report and signs of disease. Clearly articulate the findings in the structured format.
3.Recommendations: Provide recommendations based on the findings and the patient's medical history, including treatment options.
4.Treatment Suggestions: Based on the findings, suggest appropriate treatment options for the patient.

Important Notes:
1. Scope of Response: Only respond if the image pertains to human health issues.
2.Clarity of Image: In cases where the image quality impedes clear analysis, note that certain aspects are 'Unable to be determined based on the provided image.'
3. Confidentiality: Ensure that all patient information remains confidential and is not disclosed in the response.
4.Treatment Suggestions: If appropriate, recommend appropriate treatment options for the patient.
5.Disclaimer: Accompany your analysis with disclaimer: "Consult with your doctor prior to taking any prescribed medications or treatments."

Please provide me an output response with these 4 headings: "Detailed Analysis", "Findings Report", "Recommendations and Next steps", "Treatment Suggestions"
"""
#model configuration
model = genai.GenerativeModel(model_name="gemini-1.5-pro",
                              generation_config=generation_config, 
                              safety_settings=safefy_settings)
# let the page configuration

st.set_page_config(page_title="Medical Chatbot", page_icon=":robot", layout="wide")
# set the title of the page
st.title("Medical Chatbot Application")

st.subheader("An application that can help users to identify medical images")
uploaded_file = st.file_uploader("Upload an Medical image for analysis", type=["jpg", "jpeg", "png"])
if uploaded_file:
    st.image(uploaded_file, width=300, caption="Uploaded Medical Image")

submit_button = st.button("Generate the Analysis")

if submit_button:
    # making our image ready
    image_data = uploaded_file.getvalue()

    image_parts = [
        {
            "mime_type": "image/jpeg",
            "data": image_data
        }
    ]
    # making our prompt ready
    prompts_parts = [
        image_parts[0],
        system_prompts,
    ]

    ## Generate a response based on prompt and image
    response=st.title("Here is the analysis based on your image: ")
    
    if response:
        response = model.generate_content(prompts_parts)
    
        st.write(response.text)