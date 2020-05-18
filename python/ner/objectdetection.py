import os
import requests


dploy_url = "https://api.dev.dinosl1ke1cecream.dploy.ai/v1/predictions/810c94ff-dd58-48c7-8cd3-1082d6dce49d"

if __name__ == '__main__':
    api_key = os.environ['apikey']
    user_id = os.environ['userid']
    print(api_key)
    text = "Lisp (historically LISP) is a family of programming languages with a long history and a distinctive, fully parenthesized prefix notation.[3] Originally specified in 1958, Lisp is the second-oldest high-level programming language in widespread use today. Only Fortran is older, by one year.[4][5] Lisp has changed since its early days, and many dialects have existed over its history. Today, the best-known general-purpose Lisp dialects are Racket, Common Lisp, Scheme and Clojure. "
    headers = {
            'x-api-key': api_key,
            'x-api-user': user_id,
            'client-version': 'v1.0.0',
            'client': 'script',
            'content-type': 'application/json'
            }
    r = requests.post(url = dploy_url, json={"text": text}, headers = headers)
    print(r.text)
