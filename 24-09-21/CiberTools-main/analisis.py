from bs4 import BeautifulSoup
import os
import requests
import socket
import json
import argparse
import sys
import os, time, random
from progress.bar import Bar, ChargingBar
from subprocess import *
from requests import api
import scapy.all as scapy
import nmap
from pyhunter import PyHunter
from openpyxl import Workbook
import getpass






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
    parser.add_argument("-ip", dest="ip",default="8.8.4.4" ,help="Ingresa la ip, si no pones nada se tomará automatico 8.8.4.4")
    parser.add_argument("-k", dest="ip_local" ,help="Ingresa la ip")
    parser.add_argument("-d", dest="domain" ,help="Ingresa un dominio para hunter")
    ip_public = parser.parse_args()
    ip_local = parser.parse_args()
    domain = parser.parse_args()
    url = "http://free.ipwhois.io/json/{}".format(ip_public.ip)
    barra()
    soup = requests.get(url)
    data = soup.text
    data = soup.json()
    datos=open("datos.txt", "w" )
    for key in data:
        datos.write(key + ": " + str(data[key])+"\n")
    datos.close()
    print("Archivo con datos de Geolocalizacion generado con exito ")
    return ip_local, domain
    


# Funcion para scanear las ip activas en una red local 


def scan(ip):
    # Usamos argparser para pasar los argumentos por terminal
    archivo=open("ips.txt","w")
    print("Scanning...")
    # iniciamos el scaneo 
    arp_request=scapy.ARP(pdst=ip.ip_local+"/24")
    brodcast=scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp=brodcast/arp_request
    barra()
    answered=scapy.srp(arp, timeout=1,verbose=False)[0]
    # Guardamos en un txt las ip y las mac addres con un for recorriendo answered
    for element in answered:
        archivo.write("IP:{}".format(element[1].psrc))
        archivo.write("MAC address: {}\n".format(element[1].hwsrc))
    archivo.close()
    print("Archivo con ip´s activas en la red local ingresada generado con exito ")


# Se Empieza a leer el archivo que contiene las ip para almacenar en una lista


def Ports():
    lista_ip=[]
    archivo=open("ips.txt","r")
    lineas = archivo.readlines()
    for i in lineas:
        lista_ip.append((i[3:18]))
    print("Estas son las ip que puedes utilizar: -> ",lista_ip)
    archivo.close()

    # Decvlaramos listas
    lista_puertos=[80,8080,22,23,21,443,3306,53,]
    open_ports = []
    ip = input("ingresa la ip para scanear puertos: ")
    # Solicitamos la ip para escaenadr puertos
    #ip_add_entered = input("\nPlease enter the ip address that you want to scan: ")
    for port in lista_puertos:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.5)
                s.connect((ip, port))
                open_ports.append(port)
        except:
            pass
    for port in open_ports:
        print("Port {} is open on {}".format(port,ip))
    op=input("Deseas Escanear otra ip: [y]o[n]")
    while op == "y":
        Ports()
    else:
        print("Scrip Fuera")
        exit()
   

def my_ip():
    url1 = 'https://www.cual-es-mi-ip.net/'
    # Peticiones a cada uno de los links
    page1 = requests.get(url1)
    soup1 = BeautifulSoup(page1.content,"html.parser")
    origen = soup1.find_all("span",class_="big-text font-arial")
    for i in origen:
        ip_public = i.text
    code = page1.status_code
    if code == 200:
        return ip_public
    else:
        ip = ''
   

