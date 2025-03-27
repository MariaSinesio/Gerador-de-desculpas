from django.urls import path
from . import views

app_name = 'desculpas'

urlpatterns = [
    path('', views.home, name='home'),
    path('gerar/', views.gerar_desculpa, name='gerar'),
]
