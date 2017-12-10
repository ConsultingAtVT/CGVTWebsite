"""cgvt_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

from apps.core import views as core_views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('social.apps.django_app.urls', namespace='social')),

    url(r'^$', core_views.redirect_to_home),
    url(r'^about/$', core_views.about),    
    url(r'^home/$', core_views.home),
    url(r'^logout/$', core_views.logout),
    url(r'^projects/$', core_views.projects),
    url(r'^recruitment/$', core_views.recruitment),	
	url(r'^calendar/$', core_views.calendar),
	]
