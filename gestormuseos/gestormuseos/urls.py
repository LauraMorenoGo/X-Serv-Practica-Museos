from django.conf.urls import include, url
from django.contrib import admin
from museos import urls as museosurls
from museos import views



urlpatterns = [
    # Examples:
    # url(r'^$', 'gestormuseos.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^museos/', include(museosurls)),
    url(r'^usuario/', views.usuario),
    url(r'^$', views.barra)
]
