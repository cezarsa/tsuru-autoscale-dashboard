from django.conf.urls import include, url


urlpatterns = [
    url(r'^', include('tsuru_autoscale.urls')),
]
