
from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib import messages


def registrar_votacao(request):

    form = VotacaoForm()
    pessoa = Pessoa.objects.get(id=1)

    if request.method == "POST":
        form = VotacaoForm(request.POST)

        if form.is_valid():
            votacao = form.save()
            votacao.save()

            messages.success(request,"HIHIIH")

            return redirect("index")

    context = {
        "nome_pagina": "Registrar Votação",
        "form": form,
        "pessoa": pessoa,
    }

    return render(request, "cadastro/registrar_votacao.html", context)

def registrar_opcao(request):

    form = OpcaoVotoForm()

    if request.method == "POST":
        form = OpcaoVotoForm(request.POST)

        if form.is_valid():
            opcao_voto = form.save()

            opcao_voto.save()

            return redirect("index")

    context = {
        "nome_pagina": "Registrar Opção de Voto",
        "form": form,
    }

    return render(request, "cadastro/registrar_opcao.html", context)

def listar_votacoes(request):
    
    votacoes = Votacao.objects.all()

    context = {
        "votacoes": votacoes,
    }

    return render(request, "cadastro/listar_votacao.html", context)

def listar_opcoes(request):
    
    opcoes = OpcaoVoto.objects.all()

    context = {
        "opcoes": opcoes,
    }

    return render(request, "cadastro/listar_opcoes.html", context)

def detalhe_votacao(request, id_votacao):