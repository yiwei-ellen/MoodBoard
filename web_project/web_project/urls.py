"""web_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from main.views import splash, user_login, logout_, signup_ ,Page,create_card

urlpatterns = [
    path("",splash,name = 'splash'),
    path('admin', admin.site.urls),
    path('login', user_login, name='login'),
    path('logout', logout_, name='logout'),
    path('signup', signup_, name='signup'),
    path('cards', Page.as_view(), name='cards'),
    path('cardnew',create_card,name="newcard")

]
#this allows the views.py to look into the media file for input image to the emotion detection model
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)