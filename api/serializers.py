from rest_framework import serializers
from .models import Cliente, Funcionario, Operador, Servico, ServicoPrestado, Pagamento, Despesa, FluxoCaixa, Operacao, Salario

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
    servico_id = serializers.PrimaryKeyRelatedField(queryset=Servico.objects.all(), source='servico')
    cliente_id = serializers.PrimaryKeyRelatedField(queryset=Cliente.objects.all(), source='cliente')
    funcionario_id = serializers.PrimaryKeyRelatedField(queryset=Funcionario.objects.all(), source='funcionario')

    class Meta:
        model = ServicoPrestado
        fields = ['id', 'data_servico', 'valor_cobrado', 'observacoes', 'servico_id', 'cliente_id', 'funcionario_id']


class PagamentoSerializer(serializers.ModelSerializer):
    servico_prestado = serializers.PrimaryKeyRelatedField(queryset=ServicoPrestado.objects.all())
    servico_nome = serializers.CharField(source='servico_prestado.servico.nome', read_only=True)
    class Meta:
        model = Pagamento
        fields = ['id', 'servico_prestado', 'servico_nome','valor_pago', 'data_pagamento', 'metodo_pagamento', 'status']


class DespesaSerializer(serializers.ModelSerializer):
    operador_id = serializers.PrimaryKeyRelatedField(queryset=Operador.objects.all(), source='operador')

    class Meta:
        model = Despesa
        fields = ['id', 'tipo_despesa', 'valor', 'descricao', 'data_despesa', 'categoria', 'operador_id']


class FluxoCaixaSerializer(serializers.ModelSerializer):
    pagamento_id = serializers.PrimaryKeyRelatedField(queryset=Pagamento.objects.all(), source='pagamento')
    operador_id = serializers.PrimaryKeyRelatedField(queryset=Operador.objects.all(), source='operador')

    class Meta:
        model = FluxoCaixa
        fields = ['id', 'tipo_operacao', 'valor', 'descricao', 'data_operacao', 'pagamento_id', 'operador_id', 'status']


class OperacaoSerializer(serializers.ModelSerializer):
    operador_id = serializers.PrimaryKeyRelatedField(queryset=Operador.objects.all(), source='operador')
    fluxo_id = serializers.PrimaryKeyRelatedField(queryset=FluxoCaixa.objects.all(), source='fluxo')

    class Meta:
        model = Operacao
        fields = ['id', 'operador_id', 'tipo_operacao', 'descricao', 'data_operacao', 'fluxo_id', 'status']


class SalarioSerializer(serializers.ModelSerializer):
    funcionario_id = serializers.PrimaryKeyRelatedField(queryset=Funcionario.objects.all(), source='funcionario')

    class Meta:
        model = Salario
        fields = ['id', 'funcionario_id', 'valor_salario', 'data_pagamento', 'observacoes']
