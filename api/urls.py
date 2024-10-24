from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import (
    ClienteViewSet, FuncionarioViewSet, OperadorViewSet, 
    ServicoViewSet, ServicoPrestadoViewSet, PagamentoViewSet,
    DespesaViewSet, FluxoCaixaViewSet, OperacaoViewSet, SalarioViewSet
)

""" 
Pode ser feito roteamento manual dos metodos http também
"""

router = DefaultRouter()
router.register(r'clientes', ClienteViewSet, basename='cliente')
router.register(r'funcionarios', FuncionarioViewSet, basename='funcionario')
router.register(r'operadores', OperadorViewSet, basename='operador')
router.register(r'servicos', ServicoViewSet, basename='servico')
router.register(r'servicos-prestados', ServicoPrestadoViewSet, basename='servico_prestado')
router.register(r'pagamentos', PagamentoViewSet, basename='pagamento')
router.register(r'despesas', DespesaViewSet, basename='despesa')
router.register(r'fluxo-caixa', FluxoCaixaViewSet, basename='fluxo_caixa')
router.register(r'operacoes', OperacaoViewSet, basename='operacao')
router.register(r'salarios', SalarioViewSet, basename='salario')

# Inclui as rotas geradas automaticamente
urlpatterns = [
    path('/', include(router.urls)),
]
