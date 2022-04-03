import json
import requests ,base64
import os
def analyze(image_path):
    print(image_path)
    with open(image_path, "rb") as f:
        im_bytes = f.read()
    im_b64 = base64.b64encode(im_bytes).decode("utf8")
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    payload = json.dumps( { "img": ["data:image/jpeg;base64,"+ im_b64]})
    response = requests.post('http://localhost:5010/analyze', data=payload, headers=headers)
    try:
        data = response.json()
        print(data) 
        return data
    except requests.exceptions.RequestException:
        print(response.text)
        return None

img = 'img.jpg'
fg = analyze(img)
print(fg)
