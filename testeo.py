
# import requests
# import io
# from PIL import Image
# from datetime import datetime
# def text2image(prompt: str):
#     # API_URL = "https://api-inference.huggingface.co/models/kr-manish/text-to-image-sdxl-lora-dreemBooth-rashmika"
#     # API_URL = "https://api-inference.huggingface.co/models/kr-manish/text-to-image-sdxl-lora-dreemBooth-rashmika_3000_512x512"
#     API_URL = "https://api-inference.huggingface.co/models/stablediffusionapi/realistic-stock-photo-v2"

#     headers = {"Authorization": "Bearer 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"}
#     payload = {"inputs": prompt,
#     }   
#     response = requests.post(API_URL, headers = headers, json = payload)
#     image_bytes = response.content
#     print(image_bytes)
#     image = Image.open(io.BytesIO(image_bytes))
#     # timestamp =  datetime.now().strftime("%m/%d/%Y")
#     filename ="devilusewww.jpg"
#     image.save(filename)
#     return filename
# text2image("ultra realista hombre lobo vestido de traje")
import streamlit as st
import requests
import json

def generate_image():
    url = "https://modelslab.com/api/v6/images/text2img"

    payload = {
        "key": "Bearer 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",
        "model_id": "realistic-stock-photo-v2",
        "prompt": "ultra realistic close up portrait ((beautiful pale cyberpunk female with heavy black eyeliner)), blue eyes, shaved side haircut, hyper detail, cinematic lighting, magic neon, dark red city, Canon EOS R3, nikon, f/1.4, ISO 200, 1/160s, 8K, RAW, unedited, symmetrical balance, in-frame, 8K",
        "negative_prompt": "painting, extra fingers, mutated hands, poorly drawn hands, poorly drawn face, deformed, ugly, blurry, bad anatomy, bad proportions, extra limbs, cloned face, skinny, glitchy, double torso, extra arms, extra hands, mangled fingers, missing lips, ugly face, distorted face, extra legs, anime",
        "width": "512",
        "height": "512",
        "samples": "1",
        "num_inference_steps": "30",
        "safety_checker": "no",
        "enhance_prompt": "yes",
        "seed": None,
        "guidance_scale": 7.5,
        "multi_lingual": "no",
        "panorama": "no",
        "self_attention": "no",
        "upscale": "no",
        "embeddings": "embeddings_model_id",
        "lora": "lora_model_id",
        "webhook": None,
        "track_id": None
    }

    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))

    return response.json()

st.title("Generador de imágenes")
st.write("Este es un generador de imágenes utilizando el API de ModelsLab.")

if st.button("Generar imagen"):
    result = generate_image()
    if 'images' in result:
        st.image(result['images'][0]['url'], caption='Generated Image', use_column_width=True)
    else:
        st.error("No se pudo generar la imagen. Verifica la respuesta recibida.")
