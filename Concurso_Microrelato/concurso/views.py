from django.shortcuts import render
from django.http import HttpResponse
from concurso import models
# Create your views here.
def index(request):
	info = {'hola':'Aire'}
	return render(request, 'concurso/index.html',info)

def aprobarTweet(request,idT):
	aprobado=tweetCargado.objects.get(idRef=idT)
	aprobado.aprobarTweet()
	return HttpResponse('done')