from django.conf.urls import url
from . import views

app_name = 'tot'

urlpatterns = [
    url(r'^$', views.tot, name='tot'),
    url('breakage', views.breakage, name='breakage'),
    url('total', views.total, name='total'),
    url('last_chance', views.last_chance, name='last_chance')
    ]
