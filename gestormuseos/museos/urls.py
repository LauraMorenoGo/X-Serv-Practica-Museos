from django.conf.urls import include, url
from django.contrib import admin
from museos import urls as museosurls
from museos import views


urlpatterns = [
    # Examples:
    # url(r'^$', 'gestormuseos.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'(?P<id>\d+)', views.MuseoDetalle.as_view())	#Variable P que va a ser id

]
