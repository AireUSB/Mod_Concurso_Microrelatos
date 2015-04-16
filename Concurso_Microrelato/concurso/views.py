from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.
def index(request):
	info = {'hola':'Aire'}
	return render(request, 'concurso/index.html',info)

def aprobarTweet(request,idT):
	aprobado=tweetCargado.objects.get(idRef=idT)
	aprobado.aprobarTweet()
	return HttpResponse('done')

def activarCaptacion(request):
	startDaemonThread('palabra')
	return HttpResponse('Captando Tweets')

def desactivarCaptacion(request):
	stopDaemonThread()
	return HttpResponse('Captacion Detenida')

def daemonStatus(request):
	encendido = daemonThreadStatus()
	if(encendido):
		return HttpResponse('Demonio Activo')
	else:
		return HttpResponse('Demonio Inactivo')