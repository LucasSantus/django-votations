# Generated by Django 3.0.13 on 2021-06-25 14:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('votacao', '__first__'),
        ('usuarios', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa_Voto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade_votos', models.IntegerField(default=0, null=True, verbose_name='Quantidade de Votos')),
                ('opcao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='votacao.OpcaoVoto')),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.Pessoa')),
                ('votacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='votacao.Votacao')),
            ],
            options={
                'verbose_name': 'Voto Pessoa',
                'verbose_name_plural': 'Voto das Pessoas',
                'db_table': 'pessoa_voto',
            },
        ),
    ]
