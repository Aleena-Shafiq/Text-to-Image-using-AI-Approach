import requests
import base64
import streamlit as st
from PIL import Image
from io import BytesIO

headers = {'Bypass-Tunnel-Reminder': "go", 'mode': 'no-cors'}

def check_if_valid_backend(url):
    try:
        resp = requests.get(url, timeout=5, headers=headers)
        return resp.status_code == 200
    except requests.exceptions.Timeout:
        return False

def call_dalle(url, text, num_images=1):
    data = {"text": text, "num_images": num_images}
    resp = requests.post(url + "/generate", headers=headers, json=data)
    if resp.status_code == 200:
        return resp

def create_and_show_images(url, text, num_images):
    valid = check_if_valid_backend(url)
    if not valid:
        st.write("Backend service is not running")
    else:
        resp = call_dalle(url, text, num_images)
        if resp is not None:
            data = resp.json()
            generatedImgs = data['generatedImgs']
            for index in range(len(generatedImgs)):
                img = base64.b64decode(generatedImgs[index])
                image = Image.open(BytesIO(img))
                st.image(image, use_column_width=True)
                # Add CSS styling to curve the image edges
                image_style = f"""
                    <style>
                        img {{
                            border-radius: 20px;
                            margin: 10px;
                        }}
                    </style>
                """
                st.markdown(image_style, unsafe_allow_html=True)
                # Add download link
                download_link = f'<a href="data:image/png;base64,{base64.b64encode(img).decode()}" download="image{index}.png">Download Image</a>'
                st.markdown(download_link, unsafe_allow_html=True)

img=Image.open('AI.png')
col1, col2, col3,col4,col5,col6,col7,col8 = st.columns(8)

with col1:
    st.write(' ')
with col2:
      st.write(' ')
with col3:
    st.write(' ')
with col4:
    st.image(img,width=270)  
with col5:
    st.write(' ')
with col6:
    st.write(' ')
with col7:
    st.write(' ')
with col8:
    st.write(' ')
        

st.markdown("<h1 style='text-align: center;'>Text to Image Converter using Artificial Intelligence Approach</h1>", unsafe_allow_html=True)

# Insert your name

st.markdown("<div align='center'><h3><b><i>Presented To: Engr.Shahid Ali</i></b></h3></div>", unsafe_allow_html=True)
st.markdown("<div align='center'><i></i></div>", unsafe_allow_html=True)
st.markdown("<div align='center'><h3><i>Designed By: Muhammad Umer (20-CP-78) & Aleena Shafiq (20-CP-90)</h3></i></div>", unsafe_allow_html=True)
st.markdown("<div align='center'><h3><i>           </h3></i></div>", unsafe_allow_html=True)

url = st.text_input("Enter the backend URL")

text = st.text_input("What should I create?")

num_images = st.slider("How many images?", 1, 6)

ok = st.button("GO!")

if ok:
    create_and_show_images(url, text, num_images)


footer="""<style>
.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: rgb(70,73,92);
color: black;
text-align: center;
}
</style>
<div class="footer">
<p>© All Rights Reserved 2023</p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)