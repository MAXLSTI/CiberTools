from pyhunter import PyHunter
from openpyxl import Workbook
import os
import getpass
# Definimos la funcion busqueda

def busqueda(organizacion):
    # Cantidad de resultados esperados de la búsqueda
    # El límite MENSUAL de Hunter es 50, cuidado!
    resultado = hunter.domain_search(company=organizacion,
                                     limit=9, emails_type='personal')
    return resultado

# Definimos la funcion para guardar la informacion

correos=[]
def guardar_informacion(datosEncontrados, organizacion):
    #for key in datos_encontrados:
    #    print(key,":",datos_encontrados[key])
    for i in range(9):
        correos.append(datosEncontrados["emails"][i]["value"])
    print(correos)
    archivo=open("uanl.txt","w")
    for key in datosEncontrados:
        archivo.write(key+":"+str(datosEncontrados[key])+"\n")
    archivo.close()
    archivo=open("correos.txt","w")
    for i in correos:
       archivo.write(i+"\n")
    archivo.close()
archivo=open("C:/Users/mcdan/OneDrive - Universidad Autonoma de Nuevo León/2020-2021/Desktop/CLave-API.txt","r")
# Hacemos la peticion del API al usuario
print("Script para buscar información")
clave = archivo.readline()
apikey = clave
archivo.close()
hunter = PyHunter(apikey)
orga = 'uanl.mx'
datosEncontrados = busqueda(orga)

# Si nos devuelve resultados lo imprimimos en pantalla
if datosEncontrados is None:
    exit()
else:
    #print(datos_encontrados["emails"][1])
    #print(type(datos_encontrados))
    guardar_informacion(datosEncontrados, orga)
