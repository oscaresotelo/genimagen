
import requests
import io
from PIL import Image
from datetime import datetime
def text2image(prompt: str):
    # API_URL = "https://api-inference.huggingface.co/models/kr-manish/text-to-image-sdxl-lora-dreemBooth-rashmika"
    API_URL = "https://api-inference.huggingface.co/models/kr-manish/text-to-image-sdxl-lora-dreemBooth-rashmika_3000_512x512"
    headers = {"Authorization": "Bearer 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"}
    payload = {"inputs": prompt,
    }   
    response = requests.post(API_URL, headers = headers, json = payload)
    image_bytes = response.content
    print(image_bytes)
    image = Image.open(io.BytesIO(image_bytes))
    # timestamp =  datetime.now().strftime("%m/%d/%Y")
    filename ="devilusewww.jpg"
    image.save(filename)
    return filename
text2image("hombre lobo vestido de traje , caminando bajo la lluvia por un camino solitario, con la cabeza mojada y baja")