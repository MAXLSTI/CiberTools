# En esta parte nos encargamso de encriptar cada uno de los archivos que generamos en el reporte


$rutas = '.\datos.txt','.\datoss.xlsx','.\ips.txt'
$rutaencriptada = '.\Encriptado\datos.txt','.\Encriptado\datoss.xlsx','.\Encriptado\ips.txt'


$n=0
foreach ($elemento in $Rutas)
{
	$pic =  Get-Content $rutas[$n]
	$picBytes = [System.Text.Encoding]::Unicode.GetBytes($pic)
	$picEncoded = [Convert]::ToBase64String($picBytes)
	$picEncoded > $rutaencriptada[$n]
	Remove-Item $rutas[$n]
	$n=$n+1
}
