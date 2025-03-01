import os
import json
import requests

def send_bulk(payload):
    headers = {
        'X-API-KEY': os.environ.get('SMS_API'),
        'Content-Type': 'application/json'
    }

    URL = "https://api.sms.ir/v1/send/" + "bulk"
    res = requests.post(URL, json=payload, headers=headers)

    return res.json()


def send_pattern(payload):
    headers = {        
        'Content-Type': 'application/json',
        'Accept': 'text/plain',
        'x-api-key': os.environ.get('SMS_API')
    }

    URL = "https://api.sms.ir/v1/send/" + "verify"
    res = requests.post(URL, json=payload, headers=headers)
    
    return res.json()


# example bulk payload:
# payload = {
#     "lineNumber": 300000000000,
#     "messageText": "Your Text",
#     "mobiles": [
#         "Your Mobile 1",
#         "Your Mobile 2"
#     ],
#     "sendDateTime": None
# }


# example pattern payload: 
# payload = {
#     "mobile": "Mobile",
#     "templateId": "templateID",
#     "parameters": [
#         {
#             "name": "PARAMETER1",
#             "value": "000000"
#         },
#         {
#             "name": "PARAMETER2",
#             "value": "000000"    
#         }
#     ]
# }


