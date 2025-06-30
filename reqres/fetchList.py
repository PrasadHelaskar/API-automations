import json
import requests

def fetchList(i=None):
    
    if i is not None:
        url = f"https://reqres.in/api/unknown/{i}"
    else:
        url = "https://reqres.in/api/unknown"
    
    header={
         "x-api-key": "reqres-free-v1"
     }
    apiCall=requests.get(url,headers=header,timeout=5)
    responceCode=apiCall.status_code
    data=apiCall.json()
    print("Responce Cdde ",responceCode)
    if responceCode !=404:
        print(json.dumps(data,indent=2))
        print(data['data']['name'])

fetchList(23)   