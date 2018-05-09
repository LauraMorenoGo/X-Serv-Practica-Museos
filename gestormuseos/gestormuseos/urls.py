from django.conf.urls import include, url
from django.contrib import admin
from museos import urls as museosurls
from museos import views
from django.conf import settings    #Añadido de stackoverflow para conseguir que me cogiera el css
from django.conf.urls.static import static  #Añadido de stackoverflow para conseguir que me cogiera el css
from django.contrib.auth.views import logout
from django.contrib.auth.views import login

urlpatterns = [
    # Examples:
    # url(r'^$', 'gestormuseos.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^museos/', include(museosurls)),
    url(r'^usuario$', views.Usuario.as_view()),
    url(r'^usuario/(?P<id>\d+)', views.Usuario.as_view()),
    url(r'^logout', logout),
    url(r'^login', login),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^accounts/profile/(?P<id>\d+)', views.Usuario.as_view()),
    url(r'^$', views.Barra.as_view())


]





# Añadido de stackoverflow para conseguir que me cogiera el css
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)