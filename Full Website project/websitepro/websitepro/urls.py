"""websitepro URL Configuration

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
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin

from websiteapp.views import home_page,contact_page,about_page,register_page,services_page,login_page

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/', home_page),
    url(r'^contact/', contact_page),
    url(r'^about/', about_page),
    url(r'^services/', services_page),
    url(r'^registration/', register_page),
    url(r'^login/', login_page),

    url(r'^$', login_page),
]
