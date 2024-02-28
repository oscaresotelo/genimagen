# import requests  
# import json  
  
# url =  "https://imagepipeline.io/sdxl/text2image/v1/run"  
  
# payload = json.dumps({  
# "model_id":  "sdxl",  
# "prompt":  "ultra realistic close up portrait ((beautiful pale cyberpunk female with heavy black eyeliner)), blue eyes, shaved side haircut, hyper detail, cinematic lighting, magic neon, dark red city, Canon EOS R3, nikon, f/1.4, ISO 200, 1/160s, 8K, RAW, unedited, symmetrical balance, in-frame, 8K",  
# "negative_prompt":  "painting, extra fingers, mutated hands, poorly drawn hands, poorly drawn face, deformed, ugly, blurry, bad anatomy, bad proportions, extra limbs, cloned face, skinny, glitchy, double torso, extra arms, extra hands, mangled fingers, missing lips, ugly face, distorted face, extra legs, anime",  
# "width":  "512",  
# "height":  "512",  
# "samples":  "1",  
# "num_inference_steps":  "30",  
# "safety_checker":  False,   
# "guidance_scale":  7.5,  
# "multi_lingual":  "no",  
# "embeddings":  "", 
# "lora_models": "90525551-24b5-43fe-9dfc-4c6d9cffe157", 
# "lora_weights":  "0.5" 
# })  
  
# headers =  {  
# 'Content-Type':  'application/json',
# 'API-Key': 'Bearer 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'
# }  
  
# response = requests.request("POST", url, headers=headers, data=payload)  
  
# print(response.text)

import streamlit as st
import requests
import io
from PIL import Image
from datetime import datetime

def text2image(prompt: str, api_url: str):
    headers = {"Authorization": "Bearer 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"}
    payload = {"inputs": prompt}
    response = requests.post(api_url, headers=headers, json=payload)
    image_bytes = response.content
    image = Image.open(io.BytesIO(image_bytes))
    # Use la fecha y hora actual para generar el nombre del archivo
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = f"image_{timestamp}.jpg"
    image.save(filename)
    return filename

st.title("Generador De Imagenes")

prompt = st.text_input("Escribir Peticion:")
api_options = {
    "Text To Image SDXL Lora DreemBooth Rashmika": "https://api-inference.huggingface.co/models/kr-manish/text-to-image-sdxl-lora-dreemBooth-rashmika",
    "Stable Diffusion XL Base": "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0",
    "Anime": "https://api-inference.huggingface.co/models/cagliostrolab/animagine-xl-3.0"
}
selected_api = st.selectbox("Seleccione el modelo", list(api_options.keys()))

if st.button("Generar imagen"):
    with st.spinner("Generando Imagen....."):
        if prompt:
            filename = text2image(prompt, api_options[selected_api])
            st.image(filename, caption='Imagen generada', use_column_width=True)
        else:
            st.warning("Por favor, ingrese un prompt primero.")
