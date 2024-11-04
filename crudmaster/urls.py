"""
URL configuration for crudmaster project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from fichapac import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('registrarse/', views.registrarse, name='registrarse'),
    path('cerrar_sesion/', views.cerrar_sesion, name='cerrar_sesion'),
    path('iniciar_sesion/', views.iniciar_sesion, name='iniciar_sesion'),
    path('filtrar_pacientes/', views.filtrar_pacientes, name='filtrar_pacientes'),
    
    # paths de pacientes
    
    path('pacientes/', views.pacientes, name='pacientes'),
    path('añadir_paciente/', views.añadir_paciente, name='añadir_paciente'),
    path('pacientes/<int:paciente_id>', views.paciente_detail, name='paciente_detail'),
    path('pacientes/<int:paciente_id>/delete', views.delete_paciente, name='delete_paciente'),

    # paths de consultas e historia clinica
    
    path('historias/', views.historias, name='historias'),
    path('añadir_consulta/', views.añadir_consulta, name='añadir_consulta'),
    path('historias/<int:historia_id>', views.historia_detail, name='historia_detail'),
    path('historias/<int:historia_id>/delete', views.delete_historia, name='delete_historia'),
    path('filtrar_historias/', views.filtrar_historias, name='filtrar_historias'),
    path('filtrar_historias_ape/', views.filtrar_historias_ape, name='filtrar_historias_ape'),
]



