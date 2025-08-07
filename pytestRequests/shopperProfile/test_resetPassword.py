import requests
import json
from pytestRequests.jsonOperations import *

def test_resetPassword(base_attributes):
    baseUrl, header= base_attributes

    url=f"{baseUrl}/users/reset-password"

    token=json_read('TOKEN')

    extraheaders={
        "authorization": f"Bearer {token}"      
    }

    mergedHeaders={**header, **extraheaders}

    body="Datatest@1234"

    apiCall=requests.post(url=url,headers=mergedHeaders,data=body,verify=False,timeout=5)

    print("Responce Code:",apiCall.status_code)
    print("Responce Message:",apiCall.text)

    if apiCall.status_code==200:
        responce=apiCall.json()

        print("Message: ",responce['message'])
        print("data: ",responce['data'])