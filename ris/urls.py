from django.conf.urls import url
from ris import views

app_name = 'ris'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<question_id>[0-9]+)/answer/$', views.answer, name='answer'),
    ]
