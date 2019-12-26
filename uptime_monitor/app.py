import json
import os
import requests


def lambda_handler(event, context):
    url = os.environ['URL']
    try:
        resp = requests.get(url)
        if resp:
            print(f'{url} - OK')
        else:
            print(f'{url} - {resp.status_code} - ERROR')
    except requests.RequestException as e:
        print(f'{url} - ERROR')
        print(e)
        raise e
