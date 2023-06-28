import requests
import base64
import streamlit as st

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
                image_tag = f'<img src="data:image/png;base64,{base64.b64encode(img).decode()}" style="border-radius: 10px; margin: 10px;">'
                st.markdown(image_tag, unsafe_allow_html=True)
