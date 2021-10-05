

openssl enc  -aes-256-cbc -pass  file:/home/danylsti/Descargas/claves/private.key -in datos.txt -out encrypt1.txt
openssl enc  -aes-256-cbc -pass  file:/home/danylsti/Descargas/claves/private.key -in ips.txt -out encrypt2.txt
openssl enc  -aes-256-cbc -pass  file:/home/danylsti/Descargas/claves/private.key -in datoss.xlsx -out encrypt3.txt

rm -r datos.txt
rm -r ips.txt
rm -r datoss.xlsx
echo Encriptacion generada con exito 