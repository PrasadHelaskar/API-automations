import requests
import json


def test_register(base_attributes):
    baseUrl, headers = base_attributes
    zoneid= "ALPHA"
    url=f"{baseUrl}/shoppers?zoneId={zoneid}"

    body={
        "city": "Banglore",
        "country": "INDIA",
        "email": "your.email+fakedata1207@gmail.com",
        "firstName": "test",
        "gender": "MALE",
        "lastName": "test",
        "password": "Datatest@123",
        "phone": 9145678987,
        "state": "Karnataka",
        "zoneId": "ALPHA"
    }
        # to bypass CA cert you can add one more parameter as verify={value} not recommanded
    apiCall=requests.post(url=url,headers=headers,json=body,timeout=5,verify=False)

    print("Responce Code:",apiCall.status_code)

    if apiCall.status_code==201:
        responce=apiCall.json()

        print(json.dumps(responce,indent=2))

        print("ID:",responce['data']['userId'])