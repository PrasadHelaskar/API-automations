import requests

header={
    "x-api-key": "reqres-free-v1"
}

res=requests.get("https://reqres.in/api/users?page=2&delay=2",headers=header,timeout=3)

print(res.status_code)

responce=res.json()

users=responce['data']

for i in users:
    print(f"ID: {i['id']}")
    print(f"Email: {i['email']}")
    print("--"*10)