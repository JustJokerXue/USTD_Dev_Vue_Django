"""USTD_Dev_all URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from backend import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path


urlpatterns = [
                  path('login', views.login),
                  path('admin', admin.site.urls),
                  path('login/index', views.index),
                  path(r'login/infor', views.infor),
                  path(r'shenhe_delete', views.shenhe_delete),
                  path(r'login/form-editors', views.form_editor),
                  path(r'login/shenhe_get', views.shenhe_get),
                  path(r'login/shenhe_upload', views.shenhe_upload),
                  path(r'login/Academic_Early_Warning', views.academic_Early_Warning),
                  path('login/password_change_form', views.password_change_form, name='password_change_form'),
                  path(r'login/suggestion/<int:p1>', views.suggestion),
                  path('api/get_score_std', views.get_score_std)
              ]
