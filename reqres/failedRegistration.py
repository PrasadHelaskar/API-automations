import json
import requests

def failedRegistration():
    url="https://reqres.in/api/register"

    header={
        "x-api-key": "reqres-free-v1"
    }

    body={
        "email": "sydney@fife"
    }

    apiCall=requests.post(url,headers=header,json=body,timeout=5)

    print("Responce code:",apiCall.status_code)

    if apiCall.status_code ==200:
        responce=apiCall.json()
        
        print(json.dumps(responce, indent=2))

        print("ID: ",responce['id'])
        print("Token: ",responce['token'])

    else:
        print(apiCall.text)

failedRegistration()