from django.conf.urls import url
from . import views

app_name = 'child'

urlpatterns = [
    url('index/', views.index, name='index'),
    url('detail/(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    url('answer/(?P<question_id>[0-9]+)/$', views.answer, name='answer'),
    url('index_2/', views.index_2, name='index_2'),
    url('detail_2/(?P<question_id>[0-9]+)/$', views.detail_2, name='detail_2'),
    url(r'^(?P<question_id>[0-9]+)/answer_2/$', views.answer_2, name='answer_2'),
    url('index_3', views.index_3, name='index_3'),
    url('detail_3(?P<question_id>[0-9]+)/$', views.detail_3, name='detail_3'),
    url(r'^(?P<question_id>[0-9]+)/answer_3/$', views.answer_3, name='answer_3'),
    ]
