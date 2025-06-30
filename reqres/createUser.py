import json
import requests

def createUser():
    url=f"https://reqres.in/api/users"
    body={
            "name": "test_zion",
            "job": "zion resident"
        }
    header={
        "x-api-key": "reqres-free-v1"
    }

    apiCall=requests.post(url,json=body,headers=header,timeout=5)
    responceCode=apiCall.status_code
    
    print("Responce Code: ",responceCode)
    
    if responceCode == 201:
        print(json.dumps(apiCall.json(),indent=2))


createUser()