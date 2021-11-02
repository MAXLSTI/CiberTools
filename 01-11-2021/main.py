from analisis import *
logging.basicConfig(filename='info.log', level='DEBUG')


if  __name__=="__main__":
  #ip_public=my_ip()
  ip_local, ip_public, user, puertos, mensaje, numero = argumentos()
  geolocalizacion(ip_public)
  correcto = scan(ip_local)
  Ports(puertos,ip_local)
  enviar_sms(numero,mensaje)
  enviar_Correo_mamalon(user)
  paiton()
  if correcto is True:
    encrypt()
  else:
    pass
  