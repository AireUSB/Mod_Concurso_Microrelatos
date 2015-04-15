from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from concurso import views


urlpatterns = [
    # Examples:
    # url(r'^$', 'Concurso_Microrelato.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'concurso.views.index', name='index'),
    url(r'^aprobar_tweet$', 'concurso.views.aprobarTweet', name='aprobarTweet'),
    url(r'^admin/', include(admin.site.urls)),
    #static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
]
