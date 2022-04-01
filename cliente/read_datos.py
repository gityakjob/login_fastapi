import json
import requests
  
file0 = open('data.json')
dato = json.load(file0)
header = dict(Authorization= "Bearer {}".format(dato['access_token']))
r = requests.get('http://127.0.0.1:8000/', headers=header)
res_data = r.status_code
if int(res_data) == 200:
    data = json.loads(r.text)
    print(data)
else:
    print(r.text)
