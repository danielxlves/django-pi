from rest_framework import viewsets
from .models import Cliente, Funcionario, Operador, Servico, ServicoPrestado, Pagamento, Despesa, FluxoCaixa, Operacao, Salario
from .serializers import ClienteSerializer, FuncionarioSerializer, OperadorSerializer, ServicoSerializer, ServicoPrestadoSerializer, PagamentoSerializer, DespesaSerializer, FluxoCaixaSerializer, OperacaoSerializer, SalarioSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class FuncionarioViewSet(viewsets.ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer

class OperadorViewSet(viewsets.ModelViewSet):
    queryset = Operador.objects.all()
    serializer_class = OperadorSerializer

class ServicoViewSet(viewsets.ModelViewSet):
    queryset = Servico.objects.all()
    serializer_class = ServicoSerializer

class ServicoPrestadoViewSet(viewsets.ModelViewSet):
    queryset = ServicoPrestado.objects.all()
    serializer_class = ServicoPrestadoSerializer

class PagamentoViewSet(viewsets.ModelViewSet):
    queryset = Pagamento.objects.all()
    serializer_class = PagamentoSerializer

class DespesaViewSet(viewsets.ModelViewSet):
    queryset = Despesa.objects.all()
    serializer_class = DespesaSerializer

class FluxoCaixaViewSet(viewsets.ModelViewSet):
    queryset = FluxoCaixa.objects.all()
    serializer_class = FluxoCaixaSerializer

class OperacaoViewSet(viewsets.ModelViewSet):
    queryset = Operacao.objects.all()
    serializer_class = OperacaoSerializer

class SalarioViewSet(viewsets.ModelViewSet):
    queryset = Salario.objects.all()
    serializer_class = SalarioSerializer
