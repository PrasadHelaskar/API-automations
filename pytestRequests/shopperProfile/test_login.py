import requests
import json
from pytestRequests.jsonOperations import *

def test_login(base_attributes):
    baseUrl ,header=base_attributes

    url=f"{baseUrl}/users/login"

    body={
        "email": "your.email+fakedata1207@gmail.com",
        "password": "Datatest@123",
        "role": "SHOPPER"
    }

    apiCall=requests.post(url=url,headers=header,json=body,timeout=5,verify=False)

    print("Response Code:",apiCall.status_code)
    print("Response Message:",apiCall.text)

    assert apiCall.status_code==200, "The login failed"

    if apiCall.status_code==200:
        response=apiCall.json()

        print(json.dumps(response, indent=2))
        
        assert 'userId' in response['data'], "Failed to locate the User ID"

        print("ID:",response['data']['userId'])

        jwt=response['data']['jwtToken']
        
        print("Token:",jwt)

        json_update("TOKEN", jwt)
        