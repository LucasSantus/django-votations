from django.shortcuts import render
from django.utils import timezone
from votacao.models import Votacao
from usuarios.models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def base(request):
    data = timezone.now()
    
    context = { 
        'data': data.year
    }
    return context

@login_required
def index(request):
    votacoes = Votacao.objects.filter(data_inicio__lte=timezone.now(), data_fim__gte=timezone.now())
    
    if not votacoes:
        messages.info(request,"No momento não existem votações disponiveis")

    context = {
        "votacoes": votacoes,
    }
    return render(request, "home/index.html", context)