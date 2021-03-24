# Generated by Django 3.0.13 on 2021-03-24 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0003_auto_20210324_1725'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='opcaovoto',
            options={'verbose_name': 'Opcão de Voto', 'verbose_name_plural': 'Opções de Votos'},
        ),
        migrations.AlterField(
            model_name='opcaovoto',
            name='codigo',
            field=models.CharField(max_length=194, verbose_name='Código'),
        ),
        migrations.AlterField(
            model_name='opcaovoto',
            name='numero_votos',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Número de Voto'),
        ),
        migrations.AlterField(
            model_name='votacao',
            name='data_fim',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Fim do breguenait'),
        ),
        migrations.AlterField(
            model_name='votacao',
            name='data_inicio',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Inicio do breguenait'),
        ),
    ]
