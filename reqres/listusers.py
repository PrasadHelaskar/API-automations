import requests

res=requests.get("https://reqres.in/api/users?page=2")

# print(json.dumps(res.json(), indent=4))

data=res.json()

users=data['data']

for i in users:
    print(f"ID: {i['id']}")
    print(f"Email: {i['email']}")
    print("--"*10)