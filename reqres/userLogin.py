import json
import requests

def userLogin():
    url="https://reqres.in/api/login"

    header={
        "x-api-key": "reqres-free-v1"
    }
    # Remove the Password from body for unsuccessfull attempt
    body={
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }

    apiCall=requests.post(
        url,
        headers=header,
        json=body,
        timeout=5)

    print("Responce Code:",apiCall.status_code)

    if apiCall.status_code == 200:
        responce=apiCall.json()

        print(json.dumps(responce, indent=2))

        print(responce['token'])
    else:
        print(apiCall.text)

userLogin()