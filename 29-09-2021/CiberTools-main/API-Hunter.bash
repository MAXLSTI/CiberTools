
echo Ingresa el dominio del cual deceas obtener informacion
read domain
if [$domain -eq ""]
then 
    echo No ingresaste ningun valor 
fi
GET () {
curl  -i "https://api.hunter.io/v2/domain-search?domain=$domain&api_key=" > hunter.txt
}
GET
