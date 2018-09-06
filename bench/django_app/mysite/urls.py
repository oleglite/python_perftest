"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
import django

if django.VERSION[0] == 2:
    from django.urls import path
    from .views import RecordCreate, RecordRead, index
    urlpatterns = [
        path('record/create', RecordCreate.as_view()),
        path('record/read/<int:record_id>', RecordRead.as_view()),
        path('', index),
    ]
elif django.VERSION[0] == 1:
    from django.conf.urls import url
    from .views import RecordCreate, RecordRead, index
    urlpatterns = [
        url('record/create', RecordCreate.as_view()),
        url('record/read/(?P<record_id>[\d]+)', RecordRead.as_view()),
        url('', index),
    ]
