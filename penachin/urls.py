"""penachin URL Configuration

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
from django.urls import path
from home import views
urlpatterns = [
    path('', views.index,name='home'),
    path('start/', views.atualisa_status,name='start'),
    path('<int:id>', views.parar,name='parar'),
    path('admin/', admin.site.urls),
    path('dashboard/', views.dashboard, name='dashboard'),

]

admin.site.site_header = "Penachin"
admin.site.site_title = "Administração"
admin.site.index_title = "Painel admisnitrativo"
