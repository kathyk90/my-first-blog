"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
1
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^ris/', include('ris.urls')),
    url(r'^hello/', include('hello.urls')),
    url(r'^polls/', include('polls.urls')),
    url(r'^tot/', include('tot.urls')),
    url(r'^quest/', include('quest.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^child/', include('child.urls')),
    url(r'^own/', include('own.urls')),
    url(r'^quantity_3/', include('quantity_3.urls')),
    url(r'^child_6/', include('child_6.urls')),
    url(r'^child_9/', include('child_9.urls')),
    url(r'^a_6/', include('a_6.urls')),
    url(r'^a_9/', include('a_9.urls')),
    

    



    
]
