from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from concurso import views


urlpatterns = [
    # Examples:
    # url(r'^$', 'Concurso_Microrelato.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'concurso.views.index', name='index'),#index
    url(r'^aprobar_tweet/$', 'concurso.views.aprobarTweet', name='aprobarTweet'),#aprueba tweets util a futuro
    url(r'^rechazar_tweet/$', 'concurso.views.rechazarTweet', name='rechazarTweet'),#rechaza tweets util a futuro
    url(r'^update_rating/$', 'concurso.views.updateRating', name='updateRating'),#aprueba tweets util a futuro
    url(r'^activar_captacion/$', 'concurso.views.activarCaptacion', name='activarCaptacion'),#activa captacion
    url(r'^daemon_status/activar_captacion/$', 'concurso.views.activarCaptacion', name='activarCaptacion'),#activa captacion
    url(r'^desactivar_captacion/$', 'concurso.views.desactivarCaptacion', name='desactivarCaptacion'),#desactiva captacio
    url(r'^daemon_status/desactivar_captacion/$', 'concurso.views.desactivarCaptacion', name='desactivarCaptacion'),#desactiva captacio
    url(r'^daemon_status/$', 'concurso.views.daemonStatus', name='daemonStatus'),#status del demonio
    url(r'^tweets_pendientes/$', 'concurso.views.getTweetsPendientes', name='getTweetsPendientes'),#tweets pendientes
    url(r'^tweets_pendientes/aprobar/(?P<idtweet>\d+)/$', 'concurso.views.aprobarTweetURL', name='aprobarTweetURL'),#aprobar tweet
    url(r'^tweets_pendientes/rechazar/(?P<idtweet>\d+)/$', 'concurso.views.rechazarTweetURL', name='rechazarTweetURL'),#rechazar tweet
    url(r'^tweets_aprobados/$', 'concurso.views.getTweetsAprobados', name='getTweetsAprobados'),#tweets aprobados
    url(r'^top_tweets_rt/$', 'concurso.views.getTweetsPorRT', name='getTweetsPorRT'),#tweets por RT
    url(r'^top_tweets_rt/update_rt/$', 'concurso.views.updateRtCountURL', name='updateRtCountURL'),#actualizar RtCount
    url(r'^tweet_totals/$', 'concurso.views.getTweetTotals', name='getTweetTotals'),#totales tweets
    url(r'^admin/', include(admin.site.urls)),#admin site
    url(r'^accounts/login/$', 'django.contrib.auth.views.login',name='login'),#login
    url(r'^logout/$', 'django.contrib.auth.views.logout'),#logout

    #static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
]

urlpatterns += staticfiles_urlpatterns()
