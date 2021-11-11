"""in8 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from app.api.viewsets import NotebookViewSet
from app.views import iniciar_crawler

routers = DefaultRouter()
routers.register(r'notebooks', NotebookViewSet, basename='Notebook')

urlpatterns = [
    path('', include(routers.urls)),
    path('buscar/<str:modelo>/', iniciar_crawler),
    path('admin/', admin.site.urls),
]
