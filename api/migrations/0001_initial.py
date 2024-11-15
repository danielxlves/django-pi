# Generated by Django 5.1 on 2024-10-18 21:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('telefone', models.CharField(max_length=15)),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
                ('instagram_user', models.CharField(blank=True, max_length=100, null=True)),
                ('data_nascimento', models.DateTimeField(blank=True, null=True)),
                ('sexo', models.CharField(blank=True, choices=[('M', 'Masculino'), ('F', 'Feminino'), ('O', 'Outro')], max_length=1, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FluxoCaixa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_operacao', models.CharField(max_length=50)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('descricao', models.TextField()),
                ('data_operacao', models.DateTimeField()),
                ('status', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('telefone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=100)),
                ('cargo', models.CharField(blank=True, max_length=50, null=True)),
                ('salario', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('data_contratacao', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Operador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_operador', models.CharField(max_length=50, unique=True)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('senha', models.CharField(max_length=100)),
                ('tipo_operador', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Pagamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor_pago', models.DecimalField(decimal_places=2, max_digits=10)),
                ('data_pagamento', models.DateTimeField()),
                ('metodo_pagamento', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField(blank=True, null=True)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10)),
                ('duracao', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Operacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_operacao', models.CharField(max_length=50)),
                ('descricao', models.TextField()),
                ('data_operacao', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(max_length=50)),
                ('fluxo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.fluxocaixa')),
                ('operador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.operador')),
            ],
        ),
        migrations.AddField(
            model_name='fluxocaixa',
            name='operador',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.operador'),
        ),
        migrations.CreateModel(
            name='Despesa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_despesa', models.CharField(max_length=50)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('descricao', models.TextField(blank=True, null=True)),
                ('data_despesa', models.DateTimeField()),
                ('categoria', models.CharField(blank=True, max_length=50, null=True)),
                ('operador', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.operador')),
            ],
        ),
        migrations.AddField(
            model_name='fluxocaixa',
            name='pagamento',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.pagamento'),
        ),
        migrations.CreateModel(
            name='Salario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor_salario', models.DecimalField(decimal_places=2, max_digits=10)),
                ('data_pagamento', models.DateField()),
                ('observacoes', models.TextField(blank=True, null=True)),
                ('funcionario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='salarios', to='api.funcionario')),
            ],
        ),
        migrations.CreateModel(
            name='ServicoPrestado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_servico', models.DateTimeField()),
                ('valor_cobrado', models.DecimalField(decimal_places=2, max_digits=10)),
                ('observacoes', models.TextField(blank=True, null=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.cliente')),
                ('funcionario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.funcionario')),
                ('servico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.servico')),
            ],
        ),
        migrations.AddField(
            model_name='pagamento',
            name='servico_prestado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.servicoprestado'),
        ),
    ]
