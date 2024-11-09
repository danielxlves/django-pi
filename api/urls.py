from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClienteViewSet, FuncionarioViewSet, OperadorViewSet, ServicoViewSet, ServicoPrestadoViewSet, PagamentoViewSet, DespesaViewSet, FluxoCaixaViewSet, OperacaoViewSet, SalarioViewSet

router = DefaultRouter()
router.register(r'clientes', ClienteViewSet)
router.register(r'funcionarios', FuncionarioViewSet)
router.register(r'operadores', OperadorViewSet)
router.register(r'servicos', ServicoViewSet)
router.register(r'servicos-prestados', ServicoPrestadoViewSet)
router.register(r'pagamentos', PagamentoViewSet)
router.register(r'despesas', DespesaViewSet)
router.register(r'fluxos-caixa', FluxoCaixaViewSet)
router.register(r'operacoes', OperacaoViewSet)
router.register(r'salarios', SalarioViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
