from django.shortcuts import render
from django.http import HttpResponse
from .models import *
import pdb
# Create your views here.
def index(request):
	info = {'hola':'Aire'}
	return render(request, 'concurso/index.html',info)

def aprobarTweet(request):
	
	if (request.method=='POST' and 'id' in request.POST):
		aprobado=tweetCargado.objects.get(idRef=request.POST['id'])
		aprobado.aprobarTweet()
		return HttpResponse('Aprobado!')
	return HttpResponse('error')

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

def getTweetsPendientes(request):
	pendientes = getTweetsP(num=15)
	info = {'tweets':pendientes}
	return render(request, 'concurso/new_tweets.html',info) #hay q mandar solo no necesario. usar cotext con renders