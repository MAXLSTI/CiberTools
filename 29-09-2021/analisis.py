from bs4 import BeautifulSoup
import os
import requests
import socket
import json
import argparse
import sys
import os, time, random
from progress.bar import Bar, ChargingBar
from subprocess import Popen, PIPE


# Funcion para la barra de progreso 
def barra():
    bar2 = ChargingBar('Obteniendo Datos:', max=100)
    for num in range(100):
        time.sleep(random.uniform(0, 0.1))
        bar2.next()
    bar2.finish()


# Funcion para hacer la llamada a la API de Geolocalizacion
def geolocalizacion():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", dest="ip",default="8.8.4.4" ,help="Ingresa la ip, si no pones nada se tomará automatico 8.8.4.4")
    ip = parser.parse_args()
    url = "http://free.ipwhois.io/json/{}".format(ip.ip)
    barra()
    soup = requests.get(url)
    data = soup.text
    data = soup.json()
    datos=open("datos.txt", "w" )
    for key in data:
        datos.write(key + ": " + str(data[key])+"\n")
    datos.close()


# Funcion para scanear todas las ip activas de una red
def escaner():
    #ip = "192.168.0.1"
    print ("Buscando IP's")
    barra()
    ips=[]
    for r in range(1,3):
        ip = '10.0.0.19'#+str(r)
        respuesta = os.system("ping {}".format(ip))
        ips.append(respuesta)
    print(ips)
        
escaner()       



'''
#cont = 0

for ip in range(50,150):
	ipAddress = '192.168.1.'+str(ip)
	subprocess = Popen(['/bin/ping', '-c 1 ', ipAddress], stdin=PIPE, stdout=PIPE, stderr=PIPE)
	stdout, stderr= subprocess.communicate(input=None)
	if "bytes from " in stdout:
		cont +=1
		print "| "+str(cont)+" | %s | IP Activa |" %(stdout.split()[1])
		with open("ips.txt", "a") as myfile:
			myfile.write(stdout.split()[1]+'\n')
print "Total De Dispositivos Activos: " + str(cont)
'''

