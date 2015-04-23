from django.db import models
import twitter
import time
import threading
from twitter import Status, TwitterError
from django.contrib.auth.models import User
import pdb
# Create your models here.
#clase q representa un tweet para Django y la DB
class tweetCargado(models.Model):
	idRef = models.BigIntegerField(primary_key=True) 		#status.id prymary key
	userRef = models.CharField(max_length=40,default='')	#status.user.screen_name
	rtCount = models.IntegerField()							#status.retweet_count
	text =	models.CharField(max_length=200) 				#status.text
	juez1 = models.IntegerField(default=0)
	juez2 = models.IntegerField(default=0)
	juez3 = models.IntegerField(default=0)							#rating a evaluar
	ESTADO = (
		('A', 'Aprobado'), 	#tweet aprobado y concursando
		('R', 'Rechazado'), 
		('P', 'Pendiente'), #pendinte por aprobar o rechazar
	)
	estado = models.CharField(max_length=1, choices=ESTADO, default='P')

	def aprobarTweet(self):
		api=loginConcurso()
		self.estado='A'
		self.save()
		api.PostRetweet(self.idRef) #se retwitea si se aprueba

	def rechazarTweet(self):
	  self.estado='R'
	  self.save()
	
	def promedioRating(self):
		return str((self.juez1+self.juez2+self.juez3)/float(3))

	def promedioRatingInt(self):
		return (self.juez1+self.juez2+self.juez3)/float(3)
	def updateRating(self,username,opcion):
		if str(username) == "juez1":
			self.juez1=int(opcion)
		if str(username) == "juez2":
			self.juez2=int(opcion)
		if str(username) == "juez3":
			self.juez3=int(opcion)
		self.save()
		
	
	def getJuez1(self):
		return str(self.juez1)

	def getJuez2(self):
		return str(self.juez2)

	def getJuez3(self):
		return str(self.juez3)

#twiter exige autentificacion para usar su API
def loginConcurso():
	api = twitter.Api(	consumer_key='VYiMfE0d9gQJJRYF8dbtowg1b', 
						consumer_secret='43jivHqvyBWA0foMb5gHaTKs4X20YKKNgEcstP7VHMtvttSQiQ', 
						access_token_key='1367267966-j468QeDLRlDAwshy1tUJnRY55kLMHjgaJ1i6FNy', 
						access_token_secret='8Q70AkfXtH6khzcbjG9GG6aCcUA441EHTpIQLAFuCn7wv'
						)
	
	return(api)


#realiza busqueda del parametro hashtag
def buscarHT(hashtag):#busqueda completa no garantizada **verificar ID de tweet del inicio del concurso para ponerlo como 'since id ' o solucionar con streaming y hilos demonio, probar con el runserver
	api = loginConcurso()

	busqueda=api.GetSearch(term=hashtag,count=15)


	return(busqueda)

#convierte una instancia de la clase twitter.status a tweetCargado y lo guarda en la DB 
def statusToTweet(idRef_,userRef_,text_):
	nuevoTweet= tweetCargado(idRef=idRef_,userRef=userRef_,rtCount=0,text=text_,estado='P')
	nuevoTweet.save()

#convierte lista de la clase twitter.status a tweetCargado y los guarda en la DB
def statusListToTweet(statusList):
	for newTweet in statusList:
		statusToTweet(idRef_=newTweet.id, userRef_=newTweet.user.screen_name, text_=newTweet.text)

#busca y agrega a la DB lo obtenido en la busqueda del parametro 'palabra'
def searchToTweet(palabra):
	busqueda=buscarHT(palabra)
	statusListToTweet(busqueda)

#actializa el conteo de retweets de los tweets aprobados
def updateRtCount():
  tweetsAprobados=tweetCargado.objects.filter(estado='A')
  api = loginConcurso()
  for rtTweet in tweetsAprobados:
	try:    
	  rtTweet.rtCount=api.GetStatus(id=rtTweet.idRef).retweet_count
	  rtTweet.save()
	except TwitterError:
	  #Status ya no existe
	  rtTweet.rtCount=-1
	  rtTweet.save()
  return(tweetsAprobados)

#devuelve lista con tweets aprobados ordenados por su rtCount y actualizado
def getTopRt():
	aprobados = updateRtCount()
	aprobados.order_by('-rtCount')
	return (aprobados)

#imprime lista de twitter.status
def printStatusList(statusList):
	for stuff in statusList:
		print(stuff.id)

#borra todos los tweets en la DB
def deleteAllTweets():
	toDelete=tweetCargado.objects.all()
	for deleted in toDelete:
		deleted.delete()

#variables de control sobre hilo demonio
daemonThread = None
daemonStatus = 0

#metodo del hilo demonio para tweet streaming
def startTweetStream(palabra,api):
	print "Captando tweets"
	for tweet in api.GetStreamFilter(track=[palabra]):
		lastTweet = Status.NewFromJsonDict(tweet)
		statusToTweet(lastTweet.id,lastTweet.user.screen_name,lastTweet.text)
		#print lastTweet.text
		if (daemonStatus == 0):
			print "Captacion de Tweets detenida"
			return

#activa hilo demonio a captar tweets con la palabra 'busqueda'
def startDaemonThread(busqueda):
	global daemonStatus
	if(daemonStatus==0):
		api=loginConcurso()
		try:
			daemonStatus = 1
			global daemonThread
			daemonThread = threading.Thread(target=startTweetStream, args=[busqueda,api])
			daemonThread.start()
		except:
			print "Error: unable to start thread"

#desactiva hilo demonio
def stopDaemonThread():
	global daemonStatus
	daemonStatus = 0
	return

#retorna statusdel hilo 0 = apagado 1 = encendido
def daemonThreadStatus():
	global daemonStatus
	return daemonStatus

#retorna los primeros 'num' tweets pendientes
def getTweetsP(num):

	tweetsPendientes=tweetCargado.objects.filter(estado='P').order_by('idRef')
	if (len(tweetsPendientes)>=num):
		return tweetsPendientes[:num]
	else:
		return tweetsPendientes

#retorna los tweets aprobados
def getTweetsA():
	tweetsAprobados=tweetCargado.objects.filter(estado='A').extra(select={'suma':'juez1 + juez2 + juez3'}).order_by('-suma')
	return tweetsAprobados

def crearJueces():
	user = User.objects.create_user(username='juez1',
                                 email='juez1@juez1.com',
                                 password='qwerty')
	user = User.objects.create_user(username='juez2',
                                 email='juez2@juez2.com',
                                 password='asdfgh')
	user = User.objects.create_user(username='juez3',
                                 email='juez3@juez3.com',
                                 password='zxcvbn')






