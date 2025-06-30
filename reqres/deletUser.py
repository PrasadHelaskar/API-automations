import json
import requests

def deleteUser(id=None):
    if id !=None:
        url=f"https://reqres.in/api/users/{id}"
    else:
        url="https://reqres.in/api/users"

    header={
        "x-api-key": "reqres-free-v1"
    }

    apiCall=requests.delete(url,headers=header,timeout=5)

    print("Responce Code:",apiCall.status_code)

    if apiCall.status_code ==204:
        print(apiCall.text)

deleteUser(3)