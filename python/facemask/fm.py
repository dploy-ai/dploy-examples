import sys 
import os
import base64
import json
import requests

dploy_url = "https://5ad37106-34f9-44dc-a3d2-01c076ee5161.users.dev.dinosl1ke1cecream.dploy.ai/"

if __name__ == '__main__':
    # set up our tokens
    api_key = os.environ['apikey']
    user_id = os.environ['userid']

    # parse our command-line argument
    file_name = (sys.argv[-1])
    extension = file_name.split(".")[1]

    # encode our image as base64
    with open(file_name, "rb") as img:
        encoded_image = base64.b64encode(img.read())

    # set headers to include tokens (get them at api.dploy.ai)
    headers = {
            'content-type': 'application/json',
            'x-api-key': api_key,
            'x-api-user': user_id,
            }
    r  =requests.post(url = dploy_url, json={"image": encoded_image, "type": extension}, headers = headers)
    data = json.loads(r.text)
    print(data["detected_face_labels"])
