import json
import requests

nameuser = input("Nombre del usuario: ")
passwd = input("Contraseña del usuario: ")
payload = dict(username=nameuser,passwd=passwd)
r = requests.post('http://127.0.0.1:8000/auth', json=payload)
res_data = r.status_code
if int(res_data) == 200:
    data = json.loads(r.text)
    with open('data.json', 'w') as file:
        json.dump(data, file, indent=4)
    print(data['detail'])
elif int(res_data) == 403:
    data = json.loads(r.text)
    print(data['detail'])
else:
    print(r.text)

