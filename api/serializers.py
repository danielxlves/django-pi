# read_only: Campo só aparece em resposta (GET), mas não pode ser enviado no POST/PUT.
# write_only: Campo pode ser enviado, mas não aparece na resposta (ex.: senha).
# required: Define se o campo é obrigatório.
# allow_blank: Permite enviar string vazia.
# allow_null: Permite enviar nulo (null).
# default: Define valor padrão se o campo não for enviado.
# partial: Permite atualizar parcialmente com PATCH.

from rest_framework import serializers
from .models import (
    Cliente, Funcionario, Operador, Servico, 
    ServicoPrestado, Pagamento, Despesa, FluxoCaixa, 
    Operacao, Salario
)

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'


class FuncionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcionario
        fields = '__all__'


class OperadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operador
        fields = '__all__'


class ServicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servico
        fields = '__all__'


class ServicoPrestadoSerializer(serializers.ModelSerializer):
    cliente = ClienteSerializer(read_only=True)
    funcionario = FuncionarioSerializer(read_only=True)
    servico = ServicoSerializer(read_only=True)
    cliente_id = serializers.PrimaryKeyRelatedField(
        queryset=Cliente.objects.all(), source='cliente', write_only=True
    )
    funcionario_id = serializers.PrimaryKeyRelatedField(
        queryset=Funcionario.objects.all(), source='funcionario', write_only=True
    )
    servico_id = serializers.PrimaryKeyRelatedField(
        queryset=Servico.objects.all(), source='servico', write_only=True
    )

    class Meta:
        model = ServicoPrestado
        fields = ['id', 'cliente', 'funcionario', 'servico', 'data_servico', 
                  'valor_cobrado', 'observacoes', 'cliente_id', 
                  'funcionario_id', 'servico_id']


class PagamentoSerializer(serializers.ModelSerializer):
    servico_prestado = ServicoPrestadoSerializer(read_only=True)
    servico_prestado_id = serializers.PrimaryKeyRelatedField(
        queryset=ServicoPrestado.objects.all(), source='servico_prestado', write_only=True
    )

    class Meta:
        model = Pagamento
        fields = ['id', 'servico_prestado', 'servico_prestado_id', 
                  'valor_pago', 'data_pagamento', 'metodo_pagamento', 'status']


class DespesaSerializer(serializers.ModelSerializer):
    operador = OperadorSerializer(read_only=True)
    operador_id = serializers.PrimaryKeyRelatedField(
        queryset=Operador.objects.all(), source='operador', write_only=True
    )

    class Meta:
        model = Despesa
        fields = ['id', 'tipo_despesa', 'valor', 'descricao', 
                  'data_despesa', 'categoria', 'operador', 'operador_id']


class FluxoCaixaSerializer(serializers.ModelSerializer):
    pagamento = PagamentoSerializer(read_only=True)
    operador = OperadorSerializer(read_only=True)
    pagamento_id = serializers.PrimaryKeyRelatedField(
        queryset=Pagamento.objects.all(), source='pagamento', write_only=True
    )
    operador_id = serializers.PrimaryKeyRelatedField(
        queryset=Operador.objects.all(), source='operador', write_only=True
    )

    class Meta:
        model = FluxoCaixa
        fields = ['id', 'tipo_operacao', 'valor', 'descricao', 'data_operacao', 
                  'pagamento', 'pagamento_id', 'operador', 'operador_id', 'status']


class OperacaoSerializer(serializers.ModelSerializer):
    operador = OperadorSerializer(read_only=True)
    fluxo = FluxoCaixaSerializer(read_only=True)
    operador_id = serializers.PrimaryKeyRelatedField(
        queryset=Operador.objects.all(), source='operador', write_only=True
    )
    fluxo_id = serializers.PrimaryKeyRelatedField(
        queryset=FluxoCaixa.objects.all(), source='fluxo', write_only=True
    )

    class Meta:
        model = Operacao
        fields = ['id', 'operador', 'operador_id', 'tipo_operacao', 
                  'descricao', 'data_operacao', 'fluxo', 'fluxo_id', 'status']


class SalarioSerializer(serializers.ModelSerializer):
    funcionario = FuncionarioSerializer(read_only=True)
    funcionario_id = serializers.PrimaryKeyRelatedField(
        queryset=Funcionario.objects.all(), source='funcionario', write_only=True
    )

    class Meta:
        model = Salario
        fields = ['id', 'funcionario', 'funcionario_id', 'valor_salario', 
                  'data_pagamento', 'observacoes']
