from django.conf.urls import include, url
from django.contrib import admin
from museos import urls as museosurls



urlpatterns = [
    # Examples:
    # url(r'^$', 'gestormuseos.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^museos/', include(museosurls)),
]
