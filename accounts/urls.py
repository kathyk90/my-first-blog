from django.conf.urls import url, include
from . import views
from accounts import views

app_name = 'accounts'

urlpatterns = [
    url('register/', views.RegisterFormView.as_view()),
    url('login/', views.LoginFormView.as_view()),
    url('logout/', views.LogoutFormView.as_view()),
    url('questx/', views.questx, name='questx'),
    url('info/', views.info, name='info'),
    url('message/', views.message, name='message'),
    url('quant', views.quant, name='quant'),
    url('age', views.age, name='age'),
    url('about_user/', views.about_user, name='about_user'),
    url('link/', views.link, name='link'),
    url('link_2/', views.link_2, name='link_2'),
    url('tries/', views.tries, name='tries'),
    url('trai/', views.trai, name='trai'),
    url('tries_2/', views.tries_2, name='tries_2'),
    url('trai_2/', views.trai_2, name='trai_2'),
    url('creation/', views.creation, name='creation'),
    url('question/', views.question, name='question'),
    url('question_2/', views.question_2, name='question_2'),
    url('question_3/', views.question_3, name='question_3'),
    url('question_4/', views.question_4, name='question_4'),
    url('question_5/', views.question_5, name='question_5'),
    url('question_6/', views.question_6, name='question_6'),
    url('fine/', views.fine, name='fine'),
    url('contacts/', views.contacts, name='contacts'),
    ]
