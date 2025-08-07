import requests
import json
from pytestRequests.jsonOperations import *

def test_getShopper(base_attributes):
    baseUrl, headers=base_attributes
    
    shopperId=271478
    
    token=json_read('TOKEN')
    extraHeaders={
        "authorization": f"Bearer {token}"
    }
    
    url=f"{baseUrl}/shoppers/{shopperId}"

    mergedHeader={**headers , **extraHeaders}
    
    apiCall=requests.get(url=url,headers=mergedHeader,timeout=5,verify=False)

    print("\nResponse Code:",apiCall.status_code)

    if apiCall.status_code==200:
        response=apiCall.json()

        print(json.dumps(response, indent=2))

        print("First Name:",response['data']['firstName'])
        print("Token:", response['data']['jwtToken'])