from PIL import Image
import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

#genai.configure(api_key='AIzaSyAW1_N3acIUeHMH085udTt9Sk87zIbPZPE')
os.environ['GOOGLE_API_KEY'] = 'AIzaSyAW1_N3acIUeHMH085udTt9Sk87zIbPZPE'
load_dotenv()
api_key = os.getenv("AIzaSyAW1_N3acIUeHMH085udTt9Sk87zIbPZPE")
genai.configure(api_key=api_key)

safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_NONE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_NONE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_NONE"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_NONE"
    }]

import sys

# Display Python version at the top of the Streamlit app
python_version = sys.version
st.text(f"Python version: {python_version}")

img1 = st.file_uploader(label='Advert no. 1', type=['png', 'jpg'])
img2 = st.file_uploader(label='Advert no. 2', type=['png', 'jpg'])

if img1 is not None and img2 is not None:
    # Open the uploaded images
    upload_img1 = Image.open(img1)
    upload_img2 = Image.open(img2)

    model = genai.GenerativeModel('gemini-1.0-pro-vision-latest')
    
    # Process the first image
    with st.spinner('Generating content for Advert 1...'):
        response1 = model.generate_content(upload_img1)
    st.title('Advert 1')
    st.image(upload_img1)
    st.markdown(response1.text)

    
    
    # Process the second image
    with st.spinner('Generating content for Advert 2...'):
        response2 = model.generate_content(upload_img2)
    st.title('Advert 2')
    st.image(upload_img2)
    st.markdown(response2.text)
    
     

    model = genai.GenerativeModel('gemini-1.5-pro-latest')

    # Compare the advertisements
    with st.spinner('Comparing advertisements...'):
        comparison_response = model.generate_content('Compare: similarities & differences, give areas of repetition between the two advertisements, identify any creative fatigue (repetition of content)' + response1.text + response2.text)
    st.title('Comparing Advertisements')
    st.markdown(comparison_response.text)