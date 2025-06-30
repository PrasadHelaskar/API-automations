import json
import requests

def registerUser():
    url="https://reqres.in/api/register"

    header={
        "x-api-key": "reqres-free-v1"
    }

    body={
        "email": "eve.holt@reqres.in",
        "password": "pistol"
    }

    apiCall=requests.post(url,headers=header,json=body,timeout=5)

    print("Responce Code:", apiCall.status_code)


    if apiCall.status_code == 200:
        responce=apiCall.json()
        
        print(json.dumps(responce,indent=2))

        print("ID:",responce['id'])
        print("Token:",responce['token'])
    
    elif apiCall.status_code == 400:
        print(apiCall.text)

registerUser()