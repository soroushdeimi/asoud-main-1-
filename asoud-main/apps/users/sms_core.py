import os
import json
import requests

def send_verification_code(mobile: str, code: str):
    payload  = {
        "mobile": mobile,
        "templateId": "260323",
        "parameters": [
            {
                "name": "code",
                "value": code
            }
        ]
    }

    headers = {        
        'Content-Type': 'application/json',
        'Accept': 'text/plain',
        'x-api-key': os.environ.get('SMS_API')
    }
    
    URL = "https://api.sms.ir/v1/send/" + "verify"
    res = requests.post(URL, json=payload, headers=headers)
    return res.json()
    