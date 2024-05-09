from PIL import Image
import streamlit as st
import google.generativeai as genai
import time

genai.configure(api_key='AIzaSyAW1_N3acIUeHMH085udTt9Sk87zIbPZPE')

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

    #time.sleep(5) 
    
    # Process the second image
    with st.spinner('Generating content for Advert 2...'):
        response2 = model.generate_content(upload_img2)
    st.title('Advert 2')
    st.image(upload_img2)
    st.markdown(response2.text)
    
    #time.sleep(5) 

    model = genai.GenerativeModel('gemini-1.5-pro-latest')

    # Compare the advertisements
    with st.spinner('Comparing advertisements...'):
        comparison_response = model.generate_content('Compare: similarities & differences, give areas of repetition between the two advertisements, identify any creative fatigue (repetition of content)' + response1.text + response2.text)
    st.title('Comparing Advertisements')
    st.markdown(comparison_response.text)