import requests

def fetchUser(user_id):
    url=f"https://reqres.in/api/users/{user_id}"
    # header={
    #     "x-api-key": "reqres-free-v1"
    # }
    request=requests.get(url)
    print("Status code:",request.status_code)
    # print(json.dumps(request.json(), indent=2))

    data=request.json()
    print(data['data']['last_name'])


fetchUser(2)