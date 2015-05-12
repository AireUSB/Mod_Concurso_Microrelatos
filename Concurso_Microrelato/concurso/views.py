from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import *
import pdb
# Create your views here.
#@method_decorator(login_required)
@login_required(redirect_field_name='')
def index(request):
	info = {'hola':'Aire'}
	return render(request, 'concurso/index.html',info)

@login_required(redirect_field_name='')
def aprobarTweet(request):

  if (request.method=='POST' and 'id' in request.POST):
	aprobado=tweetCargado.objects.get(idRef=request.POST['id'])
	aprobado.aprobarTweet()
	return HttpResponse('Aprobado!')
	#return redirect('getTweetsPendientes')
  return HttpResponse('error')

@login_required(redirect_field_name='')
def rechazarTweet(request):

  if (request.method=='POST' and 'id' in request.POST):
	aprobado=tweetCargado.objects.get(idRef=request.POST['id'])
	aprobado.rechazarTweet()
	return HttpResponse('Rechazado!')
	#return redirect('getTweetsPendientes')
  return HttpResponse('error')

@login_required(redirect_field_name='')
def updateRating(request):

	if (request.method=='POST' and 'idTweet' in request.POST and 'opcion' in request.POST and 'username' in request.POST):
		aprobado=tweetCargado.objects.get(idRef=request.POST['idTweet'])
		aprobado.updateRating(username=request.POST['username'],opcion=request.POST['opcion'])
		return HttpResponse('Calificado!')
	return HttpResponse('error')

@login_required(redirect_field_name='')
def aprobarTweetURL(request,idtweet):
	aprobado=tweetCargado.objects.get(idRef=idtweet)
	aprobado.aprobarTweet()
	return redirect('getTweetsPendientes')

@login_required(redirect_field_name='')
def rechazarTweetURL(request,idtweet):
	rechazado=tweetCargado.objects.get(idRef=idtweet)
	rechazado.rechazarTweet()
	return redirect('getTweetsPendientes')

@login_required(redirect_field_name='')
def activarCaptacion(request):
  startDaemonThread('palabra')
  return redirect('daemonStatus')
  #return HttpResponse('Captando Tweets')
  #return render(request, "concurso/status_daemon.html", {'estado':'Activo'})

@login_required(redirect_field_name='')
def desactivarCaptacion(request):
  stopDaemonThread()
  return redirect('daemonStatus')
  #return HttpResponse('Captacion Detenida')
  #return render(request, "concurso/status_daemon.html", {'estado':'Inactivo'})

@login_required(redirect_field_name='')
def daemonStatus(request):
  encendido = daemonThreadStatus()
  if(encendido):
	info = {'estado':'Activo'}
  else:
	info = {'estado':'Inactivo'}
  return render(request, 'concurso/status_daemon.html',info)

@login_required(redirect_field_name='')
def getTweetsPendientes(request):
	pendientes = getTweetsP(num=15)
	info = {'tweets':pendientes}
	return render(request, 'concurso/new_tweets.html',info) #hay q mandar solo no necesario. usar cotext con renders

@login_required(redirect_field_name='')
def getTweetsAprobados(request):
	aprobados = getTweetsA()
	info = {'tweets':aprobados}
	return render(request, 'concurso/approved_tweets.html',info) #hay q mandar solo no necesario. usar cotext con renders

@login_required(redirect_field_name='')
def getTweetsPorRT(request):
  toptweets = getTopRt()
  toptweets.order_by('-rtCount')
  info = {'tweets':toptweets}
  return render(request, 'concurso/top_retweets.html',info) #hay q mandar solo no necesario. usar cotext con renders

@login_required(redirect_field_name='')
def getTweetTotals(request):
  info = getNumTotals()
  return render(request, 'concurso/tweet_totals.html', info)
