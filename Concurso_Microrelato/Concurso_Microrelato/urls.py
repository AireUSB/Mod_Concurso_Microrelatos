from django.conf.urls import include, url
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
    url(r'^activar_captacion/$', 'concurso.views.activarCaptacion', name='activarCaptacion'),#activa captacion
    url(r'^desactivar_captacion/$', 'concurso.views.desactivarCaptacion', name='desactivarCaptacion'),#desactiva captacio
    url(r'^daemon_status/$', 'concurso.views.daemonStatus', name='daemonStatus'),#status del demonio
    url(r'^tweets_pendientes/$', 'concurso.views.getTweetsPendientes', name='getTweetsPendientes'),#tweets pendientes
    url(r'^admin/', include(admin.site.urls)),#admin site
    url(r'^login/$', 'django.contrib.auth.views.login'),#login
    url(r'^logout/$', 'django.contrib.auth.views.logout'),#logout
    #static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
]
