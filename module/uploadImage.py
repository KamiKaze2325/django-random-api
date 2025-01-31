from io import BytesIO
from module import text2gif
import requests as r, base64

KEY = "93e921c4070e7de0b7c5a61e0053d67f"

def uploadImage(img, expiration = 60):
	data = {}
	data["key"] = KEY
	if expiration > 0:
		data["expiration"] = expiration
		
	imageB64 = base64.b64encode(img).decode()
	data["image"] = imageB64
	result = r.post("https://api.imgbb.com/1/upload", data = data).json()
	
	return result
	
	
		