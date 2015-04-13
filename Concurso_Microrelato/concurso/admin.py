from django.contrib import admin
from concurso.models import tweetCargado 


# Register your models here.


class tweetCargadoAdmin(admin.ModelAdmin):
    # ...
    list_display = ('idRef' ,'userRef', 'text')
    list_filter = ['estado']


admin.site.register(tweetCargado,tweetCargadoAdmin)