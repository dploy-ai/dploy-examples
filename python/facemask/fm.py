import sys 
import os
import base64
import json
import requests

dploy_url = "https://3345423f-8bbf-4215-8004-215a3da67b60.users.dploy.ai/"

if __name__ == '__main__':
    # set up our tokens
    api_key = os.environ['apikey']
    user_id = os.environ['userid']

    # parse our command-line argument
    file_name = (sys.argv[-1])
    extension = file_name.split(".")[-1]

    # encode our image as base64
    with open(file_name, "rb") as img:
        encoded_image = base64.b64encode(img.read()).decode('utf-8')

    # set headers to include tokens (get them at api.dploy.ai)
    headers = {
            'content-type': 'application/json',
            'x-api-key': api_key,
            'x-api-user': user_id,
            }
    r = requests.post(url = dploy_url, json={"image": encoded_image, "type": extension}, headers = headers)
    data = json.loads(r.text)

    # turn data into an image
    save_file = file_name.split(".")[0]+"_annotated" + "." + extension
    with open(save_file, "wb") as f:
        f.write(base64.b64decode(data['annotated_image']))
    print("wrote to file: " + save_file)
