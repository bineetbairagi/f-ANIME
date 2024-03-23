

import os
import google.generativeai as genai
from dotenv import load_dotenv
import streamlit as st
from PIL import Image

load_dotenv()


genai.configure(api_key = os.getenv('Gemini_Api_Key'))
def find_img(prompt,uploaded_img):
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([prompt, uploaded_img[0]])
    return response.text

def input_img_setup(uploaded_img):
    if uploaded_img is not None:
        bytes_data = uploaded_img.getvalue()
        
        image_parts = [
            {
                
                "mime_type": uploaded_img.type,
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No File Uploaded")

st.title("Welcome to :blue[f-ANIME] your anime snapping tool :)")
st.header("Upload any cutscenes of anime you want To find")
uploaded_img=st.file_uploader( type=["jpg","jpeg","png","webp"],label="" )


if uploaded_img is not None:
    try:
        image = Image.open(uploaded_img)  
        st.image(image, caption="Uploaded Image", use_column_width=True)
    except Exception as e:  
        st.error(f"Error processing image: {e}")

submit=st.button("Tell me about the anime")   

prompt='''give the name  of the anime along with description the anime in a few words,Give me the valid hyperlink to the website where we can watch it per the uploaded file.'''

if submit:
    if uploaded_img is None:
        st.error("Please upload an image before submitting.")
    else:
        image_data = input_img_setup(uploaded_img)
        response = find_img(prompt, image_data)
        st.header("The response is: ")
        st.subheader("here's what we found")
        st.write(response)
        st.info("Information provided may be inaccurate.Kindly consider double-checking the responses.")

res=st.button("Find the link")
prompt1='''give the exact hyperlink of the website where the anime is available per the uploaded file.'''
if res:
    if uploaded_img is None:
        st.error("Please upload an image before submitting.")
    else:
        image_data = input_img_setup(uploaded_img)
        response = find_img(prompt1, image_data)
        st.header("The response is: ")
        st.subheader("Here's what we found")
        st.write(response)
        st.info("Information provided may be inaccurate. Kindly consider double-checking the responses.")        

res2=st.button("Episode list")
prompt2='''from the uploaded file find the exact frame from the anime and give the most likely episode and season it is from along with its manga arc. '''
if res2:
    if uploaded_img is None:
        st.error("Please upload an image before submitting.")
    else:
        image_data = input_img_setup(uploaded_img)
        response = find_img(prompt2, image_data)
        st.header("The response is: ")
        st.subheader("Here's what we found")
        st.write(response)
        st.info("Information provided may be inaccurate. Kindly consider double-checking the responses.") 

res3=st.button("Manga finder")
prompt3='''give the exact navigable hyperlink of the website where the manga of the anime is avaiable as per the uploaded file. please dont hallucinate.'''
if res3:
    if uploaded_img is None:
        st.error("Please upload an image before submitting.")
    else:
        image_data = input_img_setup(uploaded_img)
        response = find_img(prompt3, image_data)
        st.header("The response is: ")
        st.subheader("Here's what we found")
        st.write(response)
        st.info("Information provided may be inaccurate. Kindly consider double-checking the responses.") 

footer="""<style>
a:link , a:visited;
background-color:white;
background-size: cover;
text-decoration: underline;
}

a:hover,  a:active {
color: #7A4556;
background-color:#ae3d00;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color:transparent;
color:#ae3d00;
text-align: center;
}
</style>
<div class="footer">
<p>Developed by <a text-align: justify;' href="https://www.linkedin.com/in/bineet-bairagi-a046112a2/" target="_blank">RAIDEN</a></p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)

