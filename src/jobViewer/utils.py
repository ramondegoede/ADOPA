from mimetypes import init
import requests
import json
import base64

def authorization(pat_token, response_type):
    """
    Creates the header for using api calls with PAT tokens
    """
    authorization_base64_bytes = bytes(':'+pat_token, 'ascii')
    authorization_base64_encode = base64.b64encode(authorization_base64_bytes)
    authorization_base64_string = str(authorization_base64_encode, 'ascii')

    headers = {
        'Accept': response_type,
        'Authorization': 'Basic ' + authorization_base64_string
    }
    return headers


def devopsGetApiRequest(url, authorization):
    """
    Does an API Request and returns json of that api
    """
    response = requests.get(
        url=url, 
        headers=authorization)
    response_json = json.loads(response.text)
    return response_json
