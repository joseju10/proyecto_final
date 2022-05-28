# -- Nos muestra los clubes de la liga santander. 

# -- Librerias 
import requests
import json
import os

# -- Declaración de variables
URL_BASE="https://livescore-api.com/api-client/"
KEY=os.environ["exportkey"]
SECRET=os.environ["secret"]
payload={'key':KEY,'secret':SECRET}

## -- Listado de competiciones
r_info_competiciones=requests.get(URL_BASE+'competitions/list.json',params=payload)
l_info_competiciones=r_info_competiciones.json()
lista_cod_competiciones=[]
lista_nombre_competiciones=[]
for info in l_info_competiciones["data"]["competition"]:
    if info["id"] not in lista_cod_competiciones:
        lista_nombre_competiciones.append(info["name"])
        lista_cod_competiciones.append(info["id"])

# -- PROGRAMA
payload["competition_id"]=lista_cod_competiciones[lista_nombre_competiciones.index("LaLiga Santander")]
clas_liga=requests.get(URL_BASE+"leagues/table.json?competition_id=3",params=payload)
tabla_liga=clas_liga.json()
lista1=[]
for equipo in tabla_liga["data"]["table"]:
    lista1.append(info["name"])
if len(lista1)<1:
    print("No se encontraron datos de esta liga")
else:
    print("-- Clubes: --")
    print("Club: ",lista1[0])
    print("Club: ",lista1[1])
    print("Club: ",lista1[2])
    print("Club: ",lista1[3])
    print("Club: ",lista1[4])
    print("Club: ",lista1[5])
    print("Club: ",lista1[6])
    print("Club: ",lista1[7])
    print("Club: ",lista1[8])
    print("Club: ",lista1[9])
    print("Club: ",lista1[10])
    print("Club: ",lista1[11])
    print("Club: ",lista1[12])
    print("Club: ",lista1[13])
    print("Club: ",lista1[14])
    print("Club: ",lista1[15])
    print("Club: ",lista1[16])
    print("Club: ",lista1[17])
    print("Club: ",lista1[18])
    print("Club: ",lista1[19])
