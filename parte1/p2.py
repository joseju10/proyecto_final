# -- En este programa introduces el nombre de un país y muestra todas sus competiciones nacionales
# -- Librerias necesarias
import requests
import json
import os

# -- Declaración de variables
URL_BASE="https://livescore-api.com/api-client/"
KEY=os.environ["exportkey"]
SECRET=os.environ["secret"]
payload={'key':KEY,'secret':SECRET}

# -- Información de los países
req_lista_paises=requests.get(URL_BASE+"countries/list.json",params=payload)
l_lista_paises=req_lista_paises.json()

# -- PROGRAMA
pais=input("Introduce el país del que quieres ver las diferentes ligas: " )
for info in l_lista_paises["data"]["country"]:
    lista=[]
    if info["is_real"]=="1" and pais==info["name"]:
        cad=info["leagues"].split("country=")
        payload["country"]=cad[1]
        r_lista_ligas=requests.get(URL_BASE+"leagues/list.json",params=payload)
        l_lista_ligas=r_lista_ligas.json()
        for info in l_lista_ligas["data"]["league"]:
            lista.append(info["name"])
        if len(lista)!=0:
            print(pais)
            print("-------Competiciones---------")
            for elem in lista:
                print(elem)
        else:
            print("Lo siento, no hay mas datos sobre %s" % pais)
        payload.pop('country',cad[1])