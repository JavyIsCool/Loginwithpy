'''
	Autor: PaoloRamirez
	Tema: Simple login con python a travez de metodo POST
	Link: https://www.facebook.com/PaoloProgrammer/
'''


import requests
from bs4 import BeautifulSoup

'''
	Datos generales
'''
#Proxies
proxies = {
	#"http": "",
	#"http": "",
}

#Direccion url a hacer el login
url = "http://miurl.com"

#Archivo con los datos a usar para el login
archivo = open("file1.txt","r") 

'''
	Leer datos de archivo
'''
cuenta = archivo.readline()[-1] #[:-1] elimina el salto de linea
lista_cuenta = cuenta.split(':') #split retorna una lista con los datos separados por ':'
user = lista_cuenta[0]
clave = lista_cuenta[1]

'''
	Peticion POST -> data=payload
'''

#payload es un diccionario con los datos enviados mediante post
payload = {
	#En un simple login por lo general es:
	"Usuario":user,
	"Password":clave,
	"bntEntrar":"Entrar",
}

#Envia una peticion POST
response = requests.post(url, data=payload, proxies=proxies)

#Obtiene el estado de la respuesta a la peticion
estado = response.status_code


if estado == 200:
	try:
		'''
			Analizar resultado en base a su html
		'''
		contenido = response.content
		soup = BeautifulSoup(contenido,"lxml")

		#Aqui depende del contenido del html que respondan (este sera como ejemplo)

		#Obtiene la parte del codigo html donde el id="mensaje-respuesta"
		#tambien pueden cambiarle a "class":"tipo-clase"
		datos = soup.find_all(True, {"id":"mensaje-respuesta"})

		#De la lista obtenido, tomamos los elementos
		for tag in datos:
			for linea in tag:
				linea = linea.strip()
				
				#Ejemplo de analisis de resultados
				if linea=="Cuenta correcta":
					print "User:"+user+" + Clave:"+clave+" -> Login aceptado!"

				elif linea=="Contraseña incorrecta":
					print "User:"+user+" + Clave:"+clave+" -> Contraseña incorrecta"

				else:
					print "User:"+user+" + Clave:"+clave+" -> "+linea
	except:
		print "Except:"+user+":"+clave+"\n"	

else:
	print "Error: "+str(estado)+"-> " +user+":"+clave+"\n"
	
#Cerrar archivo
archivo.close()

