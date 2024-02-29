
# import requests
# import io
# from PIL import Image
# from datetime import datetime
# def text2image(prompt: str):
#     # API_URL = "https://api-inference.huggingface.co/models/kr-manish/text-to-image-sdxl-lora-dreemBooth-rashmika"
#     API_URL = "https://api-inference.huggingface.co/models/kr-manish/text-to-image-sdxl-lora-dreemBooth-rashmika_3000_512x512"
#     headers = {"Authorization": "Bearer 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"}
#     payload = {"inputs": prompt,
#     }   
#     response = requests.post(API_URL, headers = headers, json = payload)
#     image_bytes = response.content
#     image = Image.open(io.BytesIO(image_bytes))
#     # timestamp =  datetime.now().strftime("%m/%d/%Y")
#     filename ="devilusew.jpg"
#     image.save(filename)
#     return filename
# text2image("hombre lobo, vestido de traje caminando bajo la lluvia, de noche, en un camino solitario, lleva una capucha en su cabeza")
# import streamlit as st
# import requests
# import io
# from PIL import Image
# from datetime import datetime

# def text2image(prompt: str):
#     # API_URL = "https://api-inference.huggingface.co/models/kr-manish/text-to-image-sdxl-lora-dreemBooth-rashmika"
#     API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
#     # API_URL = "https://api-inference.huggingface.co/models/kr-manish/text-to-image-sdxl-lora-dreemBooth-rashmika_3000_512x512"
#     headers = {"Authorization": "Bearer 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"}
#     payload = {"inputs": prompt}
#     response = requests.post(API_URL, headers=headers, json=payload)
#     image_bytes = response.content
#     print(image_bytes)
#     image = Image.open(io.BytesIO(image_bytes))
#     # Use la fecha y hora actual para generar el nombre del archivo
#     timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
#     filename = f"image_{timestamp}.jpg"
#     image.save(filename)
#     return filename

# st.title("Generador De Imagenes")

# prompt = st.text_input("Escribir Peticion:")
# if st.button("Generar imagen"):
#     with st.spinner("Generando Imagen....."):
#         if prompt:
#             filename = text2image(prompt)
            
#             st.image(filename, caption='Imagen generada', use_column_width=True)
#         else:
#             st.warning("Por favor, ingrese un prompt primero.")
# import streamlit as st
# import requests
# import io
# from PIL import Image
# from datetime import datetime

# def text2image(prompt: str):
#     # API_URL = "https://api-inference.huggingface.co/models/kr-manish/text-to-image-sdxl-lora-dreemBooth-rashmika"
#     API_URL = "https://api-inference.huggingface.co/models/kr-manish/text-to-image-sdxl-lora-dreemBooth-rashmika_3000_512x512"
#     headers = {"Authorization": "Bearer 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"}
#     payload = {"inputs": prompt}
#     response = requests.post(API_URL, headers=headers, json=payload)
    
#     # Verificar si la respuesta es un archivo de imagen válido
#     if response.headers.get('content-type') == 'image/jpeg':
#         image_bytes = response.content
#         image = Image.open(io.BytesIO(image_bytes))
#         # Use la fecha y hora actual para generar el nombre del archivo
#         timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
#         filename = f"image_{timestamp}.jpg"
#         image.save(filename)
#         return filename
#     else:
#         st.error("No se pudo generar la imagen. Por favor, intente nuevamente o revise el prompt proporcionado.")

# st.title("Generador de Imagenes")

# prompt = st.text_input("Escriba su Peticion:")
# if st.button("Generar imagen"):
#     with st.spinner("Generando Imagen......"):
#         if prompt:
#             filename = text2image(prompt)
#             if filename:
#                 st.image(filename, caption='Imagen generada', use_column_width=True)
#         else:
#             st.warning("Por favor, ingrese un prompt primero.")
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
    "Anime": "https://api-inference.huggingface.co/models/cagliostrolab/animagine-xl-3.0",
    "Realista": "https://api-inference.huggingface.co/models/stablediffusionapi/realistic-stock-photo-v2",
    "Piel": "https://api-inference.huggingface.co/models/shindi/realistic-skin-style"
}
selected_api = st.selectbox("Seleccione el modelo", list(api_options.keys()))

if st.button("Generar imagen"):
    with st.spinner("Generando Imagen....."):
        if prompt:
            filename = text2image(prompt, api_options[selected_api])
            st.image(filename, caption='Imagen generada', use_column_width=True)
        else:
            st.warning("Por favor, ingrese un prompt primero.")
