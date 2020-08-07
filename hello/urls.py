from django.conf.urls import url
from hello import views

app_name = 'hello'

urlpatterns = [
url('tipe', views.tipe, name='tipe'),
url('tipe_2', views.tipe_2, name='tipe_2'),
url('quest', views.quest, name='quest'),
url(r'^$', views.hello, name='hello'),
url('hello_2', views.hello_2, name='hello_2'),
url('hello_3', views.hello_3, name='hello_3'),
url('hello_4', views.hello_4, name='hello_4'),
url('hello_5', views.hello_5, name='hello_5'),
url('hello_6', views.hello_6, name='hello_6'),
url('hello_7', views.hello_7, name='hello_7'),
url('hello_8', views.hello_8, name='hello_8'),
url('creat', views.creat, name='creat'),
url('go', views.go, name='go'),
]
