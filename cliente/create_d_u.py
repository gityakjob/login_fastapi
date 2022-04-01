import json
import requests
  
file0 = open('data.json')
dato = json.load(file0)
print("Rellene los siguientes campos sobre el registro del usuario: ")
del_upd = input("Crear y actualizar (1), eliminar (2), nada (): ")
if del_upd == "1":
    nameuser = input("Nombre: ")
    passwd = input("Contraseña: ")
    superuser = input("Es administrador, si o no: ")
    adviser = input("Es asesor, si o no: ")
    active = input("Es activo, si o no (por defecto es si): ")
    is_superuser, is_adviser, is_active = False, False, True
    if superuser == "si":
        is_superuser = True
    if adviser == "si":
        is_adviser = True
    if active == "no":
        is_active = False
    us = dict(username=nameuser,passwd=passwd)
    ru = dict(is_superuser=is_superuser,is_adviser=is_adviser,is_active=is_active)
    header = dict(Authorization= "Bearer {}".format(dato['access_token']))
    payload = dict(us=us, ru=ru)
    r = requests.post('http://127.0.0.1:8000/reguser', headers=header, json=payload)
if del_upd == "2":
    nameuser = input("Nombre: ")
    header = dict(Authorization= "Bearer {}".format(dato['access_token']))
    payload = dict(username=nameuser,passwd="")
    r = requests.post('http://127.0.0.1:8000/deluser', headers=header, json=payload)
try:
    res_data = r.status_code
    if int(res_data) == 200:
        data = json.loads(r.text)
        print(data)
    elif int(res_data) == 403 or int(res_data) == 401 :
        data = json.loads(r.text)
        print(data['detail'])
    else:
        print(r.text)
except:
    print("No data")