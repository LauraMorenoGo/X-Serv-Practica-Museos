from django.conf.urls import include, url
from django.contrib import admin
from museos import urls as museosurls
from museos import views


urlpatterns = [
    # Examples:
    # url(r'^$', 'gestormuseos.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.Museos.as_view()),
    url(r'(?P<id>\d+)', views.MuseoDetalle.as_view()),	#Variable P que va a ser id
    url(r'(?P<id>\d+)/addfavorito', views.Add.as_view()),
    url(r'(?P<id>\d+)/removefavorito', views.Remove.as_view())
]
