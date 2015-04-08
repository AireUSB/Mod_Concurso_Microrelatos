from django.db import models
import twitter
# Create your models here.

class tweetCargado(models.Model):
    idRef = models.BigIntegerField() 							#status.id
    userRef = models.CharField(max_length=40,default='')	#status.user.screen_name
    rtCount = models.IntegerField()							#status.retweet_count
    text =	models.CharField(max_length=200) 				#status.text
    rating = models.IntegerField()							#rating a evaluar
    ESTADO = (
        ('A', 'Aprobado'),
        ('R', 'Rechazado'),
        ('P', 'Pendiente'),
    )
    estado = models.CharField(max_length=1, choices=ESTADO,default='P')

def loginConcurso():
	api = twitter.Api(	consumer_key='VYiMfE0d9gQJJRYF8dbtowg1b', 
						consumer_secret='43jivHqvyBWA0foMb5gHaTKs4X20YKKNgEcstP7VHMtvttSQiQ', 
						access_token_key='1367267966-j468QeDLRlDAwshy1tUJnRY55kLMHjgaJ1i6FNy', 
						access_token_secret='8Q70AkfXtH6khzcbjG9GG6aCcUA441EHTpIQLAFuCn7wv'
						)
	
	return(api)



def buscarHT(hashtag):
	api = loginConcurso()
	busqueda=api.GetSearch(term=hashtag)
	return(busqueda)

def statusToTweet(idRef_,userRef_,text_):
	nuevoTweet= tweetCargado(idRef=idRef_,userRef=userRef_,rtCount=0,text=text_,rating=0,estado='P')
	nuevoTweet.save()

def statusListToTweet(statusList):
	for newTweet in statusList:
		statusToTweet(idRef_=newTweet.id, userRef_=newTweet.user.screen_name, text_=newTweet.text)

def searchToTweet(palabra):
	busqueda=buscarHT(palabra)
	statusListToTweet(busqueda)
	



