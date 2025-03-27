from django.shortcuts import render
from django.http import JsonResponse
from .models import PedidoDesculpa
import random

def home(request):
    return render(request, 'desculpas/home.html')

def gerar_desculpa(request):
    count = PedidoDesculpa.objects.count()
    random_index = random.randint(0, count - 1)
    desculpa = PedidoDesculpa.objects.all()[random_index]
    if desculpa:
        return JsonResponse({
            'desculpa': desculpa.text,
            'color': desculpa.color
        })
    return JsonResponse({
        'desculpa': 'Sem tempo, irmao.',
        'color': '#00000'
    })

# Create your views here.
