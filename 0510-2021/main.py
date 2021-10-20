from analisis import *


if  __name__=="__main__":
   #ip_public=my_ip()
   domain,user, password,ip, domain = geolocalizacion()
   if ip.ip_local is None:
      print("Error no ingresaste el parametro -k usa --help para mas informacion ")
      exit()
   else:
      print("Iniciando scaneo ")
      scan(ip) 
      Ports()
      encrypt()
      #if user.user_name is None or password.passw is None:
      #   print("Error no agregaste los parametos user:password usa --help para mas informacin ")
      #   exit()
      #else:
      #   enviarcorreo(user,password)
    
   