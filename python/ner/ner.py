import os
import requests
import json


# endpoint to query - you can get this on the market place of dploy.ai
dploy_url = "https://aabe6e56-0fa0-44c6-8808-bed76b3413dc.users.dploy.ai/predict/"

if __name__ == '__main__':
    # set your environment variables for storing the api key and user id token. 
    # alternatively, replace these lines with the actual values
    api_key = os.environ['apikey']
    user_id = os.environ['userid']
    text = "Lisp (historically LISP) is a family of programming languages with a long history and a distinctive, fully parenthesized prefix notation.[3] Originally specified in 1958, Lisp is the second-oldest high-level programming language in widespread use today. Only Fortran is older, by one year.[4][5] Lisp has changed since its early days, and many dialects have existed over its history. Today, the best-known general-purpose Lisp dialects are Racket, Common Lisp, Scheme and Clojure. "
    # these headers need to be present to authorize requests
    headers = {
            'content-type': 'application/json',
            'x-api-key': api_key,
            'x-api-user': user_id,
            }
    r = requests.post(url = dploy_url, json={"text": text}, headers = headers)
    data = json.loads(r.text)
    print(data["annotated_text"])
