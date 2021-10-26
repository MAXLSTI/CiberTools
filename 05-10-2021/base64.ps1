# En esta parte nos encargamso de encryptar cada uno de los archivos que generamos en el reporte
$pic =  Get-Content 'C:/Users/mcdan/OneDrive - Universidad Autonoma de Nuevo León/2020-2021/Desktop/PIA/CiberTools/05-10-2021/datos.txt'
$picBytes = [System.Text.Encoding]::Unicode.GetBytes($pic)
$picEncoded = [Convert]::ToBase64String($picBytes)
$picEncoded > 'C:/Users/mcdan/OneDrive - Universidad Autonoma de Nuevo León/2020-2021/Desktop/PIA/CiberTools/05-10-2021/Encriptado/datos.txt'

$pic =  Get-Content 'C:/Users/mcdan/OneDrive - Universidad Autonoma de Nuevo León/2020-2021/Desktop/PIA/CiberTools/05-10-2021/datoss.xlsx'
$picBytes = [System.Text.Encoding]::Unicode.GetBytes($pic)
$picEncoded = [Convert]::ToBase64String($picBytes)
$picEncoded > 'C:/Users/mcdan/OneDrive - Universidad Autonoma de Nuevo León/2020-2021/Desktop/PIA/CiberTools/05-10-2021/Encriptado/datoss.xlsx'

$pic =  Get-Content 'C:/Users/mcdan/OneDrive - Universidad Autonoma de Nuevo León/2020-2021/Desktop/PIA/CiberTools/05-10-2021/ips.txt'
$picBytes = [System.Text.Encoding]::Unicode.GetBytes($pic)
$picEncoded = [Convert]::ToBase64String($picBytes)
$picEncoded > 'C:/Users/mcdan/OneDrive - Universidad Autonoma de Nuevo León/2020-2021/Desktop/PIA/CiberTools/05-10-2021/Encriptado/ips.txt'

$pic =  Get-Content 'C:/Users/mcdan/OneDrive - Universidad Autonoma de Nuevo León/2020-2021/Desktop/PIA/CiberTools/05-10-2021/Puertos_scaneado.txt'
$picBytes = [System.Text.Encoding]::Unicode.GetBytes($pic)
$picEncoded = [Convert]::ToBase64String($picBytes)
$picEncoded > 'C:/Users/mcdan/OneDrive - Universidad Autonoma de Nuevo León/2020-2021/Desktop/PIA/CiberTools/05-10-2021/Encriptado/Puertos_scaneado.txt'

$pic =  Get-Content 'C:/Users/mcdan/OneDrive - Universidad Autonoma de Nuevo León/2020-2021/Desktop/PIA/CiberTools/05-10-2021/ips.txt'
$picBytes = [System.Text.Encoding]::Unicode.GetBytes($pic)
$picEncoded = [Convert]::ToBase64String($picBytes)
$picEncoded > 'C:/Users/mcdan/OneDrive - Universidad Autonoma de Nuevo León/2020-2021/Desktop/PIA/CiberTools/05-10-2021/Encriptado/ips.txt'
# Finalmente en esta parte eliminamos los archivos no encryptados 
Remove-Item 'C:/Users/mcdan/OneDrive - Universidad Autonoma de Nuevo León/2020-2021/Desktop/PIA/CiberTools/05-10-2021/datos.txt'
Remove-Item 'C:/Users/mcdan/OneDrive - Universidad Autonoma de Nuevo León/2020-2021/Desktop/PIA/CiberTools/05-10-2021/datoss.xlsx'
Remove-Item 'C:/Users/mcdan/OneDrive - Universidad Autonoma de Nuevo León/2020-2021/Desktop/PIA/CiberTools/05-10-2021/Encriptado/ips.txt'
Remove-Item 'C:/Users/mcdan/OneDrive - Universidad Autonoma de Nuevo León/2020-2021/Desktop/PIA/CiberTools/05-10-2021/Puertos_scaneado.txt'
Remove-Item 'C:/Users/mcdan/OneDrive - Universidad Autonoma de Nuevo León/2020-2021/Desktop/PIA/CiberTools/05-10-2021/ips.txt'