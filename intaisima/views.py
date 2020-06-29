from django.http import HttpResponse #importar utileria descompuesta http
from datetime import datetime

def hello_world(request):
	now =datetime.now(). strftime('%b %dth, %y - %H:%M hrs')
	print (now)
	return HttpResponse("Hello, word: La hora del servidor es {now}".format(now=str(now)))
# funcion obtener usuario y edad 
def say_hi(request, name, age):
	if age < 13:
		mensaje = "Lo siento! {} no puedes acceder aqui".format(name)
	else:
		mensaje = "Bienvenido {}".format(name)
	return HttpResponse(mensaje)
			
	