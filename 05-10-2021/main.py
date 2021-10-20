from analisis import *


if  __name__=="__main__":
   #ip_public=my_ip()
   ip_local, ip_public, domain, user, puertos, mensaje, numero = argumentos()
   geolocalizacion(ip_local)
   if ip_public is None:
      print("Error no ingresaste el parametro -k usa --help para mas informacion ")
      exit()
   else:
      print("Iniciando scaneo ")
      scan(ip_local) 
      Ports(ip_local, puertos)
      #encrypt()
      enviar(user)
      enviar_sms(numero,mensaje)
  
   