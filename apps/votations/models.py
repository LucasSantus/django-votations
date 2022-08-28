from django.db import models
from .models import *

import string
import random

class Room(models.Model):
    title = models.CharField(verbose_name = "Título", max_length = 100)
    description = models.TextField(verbose_name = "Descrição", max_length = 2000)
    code = models.CharField(verbose_name = "Código", max_length = 30, unique = True, null = True, blank = True)
    users = models.ManyToManyField("users.User", verbose_name = "Usuários", blank = True)
    admin = models.ForeignKey("users.User", on_delete = models.CASCADE, verbose_name = "Administrador", related_name = "admin_Rooms_FK", null = True, blank = True,)
    is_active = models.BooleanField(default = True)
    create_at = models.DateTimeField(verbose_name = "Data da Criação", auto_now_add = True)

    class Meta:
        verbose_name = "Sala de Votação"
        verbose_name_plural = "Salas de Votações"
        db_table = "rooms"
        app_label = "votations"

    def get_generated_code():
        code = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(16))
        if Room.objects.get(code = code).exists():
            self.get_generated_code()
        return code

        # valid = True
        # while valid == True:
        #     try:
        #         code = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(16))
        #         Room.objects.get(code = code)
        #     except Room.DoesNotExist:
        #         valid = False
        #         return code

    def __str__(self):
        return self.title

class Votation(models.Model):
    titulo = models.CharField(verbose_name = "Título", max_length = 150)
    description = models.TextField(verbose_name = "Descrição", max_length = 2000)
    date_init = models.DateTimeField(verbose_name = "Inicio", auto_now = False, blank = True, null = True)
    date_end = models.DateTimeField(verbose_name = "Término", auto_now = False, blank = True, null = True)
    rooms = models.ForeignKey("votations.Room", verbose_name = "Sala de Votação", on_delete = models.CASCADE, null = True, blank = True)
    is_user_anonimous = models.BooleanField(verbose_name = "Usuário Anônimo", default = False,)
    is_active = models.BooleanField(default = True)
    create_at = models.DateTimeField(verbose_name = "Data da Criação", auto_now_add = True)

    class Meta:
        verbose_name = "Votação"
        verbose_name_plural = "Votações"
        db_table = "votations"
        app_label = "votations"

    def get_qtd_votacoes(self, list_salas, list_votacoes):
        vinculo = []
        if list_salas:
            qtd_votacoes = 0
            for sala in list_salas:
                qtd_votacoes = len(list_votacoes.filter(sala=sala))
                obj = {
                    "sala": sala,
                    "qtd_votacoes": qtd_votacoes,
                }
                vinculo.append(obj)
        return vinculo

    def format_date(data):
        date_list = []
        for a in range(16):
            if data[a] != '+' or data[a] != ' ':
                date_list.append(data[a])
            else:
                break
        return "".join(date_list)

    def __str__(self):
        return self.title

# class OpcaoVoto(models.Model):
#     nome = models.CharField(
#         verbose_name = "Nome",
#         max_length = 150,
#     )

#     votacao = models.ForeignKey(
#         Votacao,
#         verbose_name = "Votação",
#         on_delete = models.CASCADE,
#         null = True,
#         blank = True,
#     )

#     codigo = models.CharField(
#         verbose_name = "Código",
#         max_length = 10,
#     )

#     numero_votos = models.PositiveSmallIntegerField(
#         verbose_name = "Número de Voto",
#         default = 0,
#         null = True,
#         blank = True,
#     )

#     is_active = models.BooleanField(
#         default=True
#     )

#     data_registrado = models.DateTimeField(
#         verbose_name = "Data da Criação",
#         auto_now_add = True,
#     )

#     class Meta:
#         verbose_name = "Opcão de Voto"
#         verbose_name_plural = "Opções de Votos"

#     def __str__(self):
#         return self.nome

# class PessoaVoto(models.Model):
    # usuario = models.ForeignKey(
    #     Usuario, 
    #     on_delete = models.CASCADE
    # )

    # votacao = models.ForeignKey(
    #     Votacao, 
    #     on_delete = models.CASCADE
    # )

    # opcao_voto = models.ForeignKey(
    #     OpcaoVoto, 
    #     on_delete = models.CASCADE
    # )

    # quantidade_votos = models.IntegerField(
    #     verbose_name = "Quantidade de Votos",
    #     null = True,
    #     default = 0,
    # )
    
    # is_active = models.BooleanField(
    #     default=True
    # )

    # data_registrado = models.DateTimeField(
    #     verbose_name = "Data da Criação",
    #     auto_now_add = True,
    # )

    # class Meta:
    #     verbose_name = "Voto da Pessoa"
    #     verbose_name_plural = "Votos das Pessoas"

    # def __str__(self):
    #     return self.votacao.nome