from django.conf.urls import include, url
from django.contrib import admin
<<<<<<< HEAD
from museos import urls as museosurls
from museos import views
=======
>>>>>>> 80364828b85845e82600acf56158998f81151ec3

urlpatterns = [
    # Examples:
    # url(r'^$', 'gestormuseos.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'', include(admin.site.urls)),
<<<<<<< HEAD
    url(r'^museos/id', views.museo)
=======
>>>>>>> 80364828b85845e82600acf56158998f81151ec3
]
