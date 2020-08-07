from django.conf.urls import url
from . import views

app_name = 'child_9'

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
    url('index_4', views.index_4, name='index_4'),
    url('detail_4(?P<question_id>[0-9]+)/$', views.detail_4, name='detail_4'),
    url(r'^(?P<question_id>[0-9]+)/answer_4/$', views.answer_4, name='answer_4'),
    url('index_5', views.index_5, name='index_5'),
    url('detail_5(?P<question_id>[0-9]+)/$', views.detail_5, name='detail_5'),
    url(r'^(?P<question_id>[0-9]+)/answer_5/$', views.answer_5, name='answer_5'),
    url('index_6', views.index_6, name='index_6'),
    url('detail_6(?P<question_id>[0-9]+)/$', views.detail_6, name='detail_6'),
    url(r'^(?P<question_id>[0-9]+)/answer_6/$', views.answer_6, name='answer_6'),
    url('index_7', views.index_7, name='index_7'),
    url('detail_7(?P<question_id>[0-9]+)/$', views.detail_7, name='detail_7'),
    url(r'^(?P<question_id>[0-9]+)/answer_7/$', views.answer_7, name='answer_7'),
    url('index_8', views.index_8, name='index_8'),
    url('detail_8(?P<question_id>[0-9]+)/$', views.detail_8, name='detail_8'),
    url(r'^(?P<question_id>[0-9]+)/answer_8/$', views.answer_8, name='answer_8'),
    url('index_9', views.index_9, name='index_9'),
    url('detail_9(?P<question_id>[0-9]+)/$', views.detail_9, name='detail_9'),
    url(r'^(?P<question_id>[0-9]+)/answer_9/$', views.answer_9, name='answer_9')
    ]
