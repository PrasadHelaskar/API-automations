import json
import requests


def updateUser(id=None):
    if id !=None:
        url=f"https://reqres.in/api/users/{id}"
    else:
        url="https://reqres.in/api/users"

    header= {
        "x-api-key": "reqres-free-v1"
    }
    
    body= {
        "name": "morpheus",
        "job": "zion resident"
    }
    
    apiCall=requests.put(url,headers=header,json=body,timeout=5)

    print("Responce Code :", apiCall.status_code)

    if apiCall.status_code == 200:
        responce=apiCall.json()
        print(json.dumps(responce,indent=2))

        print("Name: ", responce['name'])
        print("job: ", responce['job'])


updateUser(3)