from django.db import models
import twitter
# Create your models here.
#clase q representa un tweet para Django y la DB
class tweetCargado(models.Model):
    idRef = models.BigIntegerField(primary_key=True) 		#status.id prymary key
    userRef = models.CharField(max_length=40,default='')	#status.user.screen_name
    rtCount = models.IntegerField()							#status.retweet_count
    text =	models.CharField(max_length=200) 				#status.text
    rating = models.IntegerField()							#rating a evaluar
    ESTADO = (
        ('A', 'Aprobado'), 	#tweet aprobado y concursando
        ('R', 'Rechazado'), 
        ('P', 'Pendiente'), #pendinte por aprobar o rechazar
    )
    estado = models.CharField(max_length=1, choices=ESTADO, default='P')

    def aprobarTweet(self, api):
    	self.estado='A'
    	self.save()
    	#api.PostRetweet(self.idRef) #se retwitea si se aprueba

	def rechazarTweet(self):
		self.estado='R'
		self.save()

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
	nuevoTweet= tweetCargado(idRef=idRef_,userRef=userRef_,rtCount=0,text=text_,rating=0,estado='P')
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
		rtTweet.rtCount=api.GetStatus(id=rtTweet.idRef).retweet_count
		return(tweetsAprobados)

#devuelve lista con tweets aprobados ordenados por su rtCount y actualizado
def getTopRt():
	aprobados = updateRtCount()
	aprobados.order_by('rtCount')
	return (aprobados)

def printStatusList(statusList):
	for stuff in statusList:
		print(stuff.id)

"""while (True):
    stream = apiTest.GetStreamFilter(None, ['someWord'])
    try:
        print(stream.next())
    except:
        print ("No posts")

    time.sleep(3)
    """






