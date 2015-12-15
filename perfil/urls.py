from django.conf.urls import patterns, include, url
from .views import index, createuser,createproject

urlpatterns = patterns('',
 
    #url(r'^$', 'perfil.views.index'),
    #url(r'^perfil/$', 'perfil.views.createuser',name="Ingresar_usuario" ),
    url(r'^$', 'perfil.views.createuser',name="Ingresar_usuario" ),

    #url(r'^$', 'perfil.views.index'),
    #url(r'^perfil/$', 'perfil.views.createproject',name="Ingresar_proyecto" ),
    url(r'^project/$', 'perfil.views.createproject',name="Ingresar_proyecto" ),
  
   #url(r'^gracias/$', graciasIdea.as_view(),name="gracias_idea" ),
   # url(r'^$', autenticate.as_view(),name="autenticar_idea" ),
   # url('', include('social.apps.django_app.urls', namespace='social')),
   # url('', include('django.contrib.auth.urls', namespace='social')),
)