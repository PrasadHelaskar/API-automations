import requests
import json
from pytestRequests.jsonOperations import *

def test_updateShopper(base_attributes):
    baseUrl, header=base_attributes
    shopperId=271478
    
    url=f"{baseUrl}/shoppers/{shopperId}"

    token=json_read('TOKEN')

    extraheader={
        "authorization": f"Bearer {token}"
    }

    mergedHeaders={**header,**extraheader}

    body={
            "city": "Banglore",
            "country": "India",
            "email": "your.email+fakedata0707noshow@gmail.com",
            "firstName": "test_fakedata",
            "gender": "MALE",
            "lastName": "lastname",
            "password": "Datatest@123",
            "phone": 9145678987,
            "state": "Karnataka",
            "zoneId": "string"
    }

    apiCall=requests.patch(url=url,headers=mergedHeaders,json=body,verify=False,timeout=5)

    print("Responce Code:", apiCall.status_code)
    # print("Responce Message:",apiCall.text)

    if apiCall.status_code ==200:
        responce=apiCall.json()

        print(json.dumps(responce, indent=2))

        print("Token:",responce.get('data',{}).get('jwtToken'))
