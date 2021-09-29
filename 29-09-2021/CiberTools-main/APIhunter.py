from pyhunter import PyHunter
from openpyxl import Workbook
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
        correos.append(datos_encontrados["emails"][i]["value"])
    print(correos)
    archivo=open("uanl.txt","w")
    for key in datos_encontrados:
        archivo.write(key+":"+str(datos_encontrados[key])+"\n")
    archivo.close()
    archivo=open("correos.txt","w")
    for i in correos:
       archivo.write(i+"\n")
    archivo.close()
# Hacemos la peticion del API al usuario
print("Script para buscar información")
apikey = input("Ingresa tu API key: ")
hunter = PyHunter(apikey)
orga = input("Dominio a investigar: ")
datos_encontrados = busqueda(orga)

# Si nos devuelve resultados lo imprimimos en pantalla
if datos_encontrados is None:
    exit()
else:
    #print(datos_encontrados["emails"][1])
    #print(type(datos_encontrados))
    guardar_informacion(datos_encontrados, orga)
