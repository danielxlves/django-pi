from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)
    email = models.EmailField(max_length=100, blank=True, null=True)
    instagram_user = models.CharField(max_length=100, blank=True, null=True)
    data_nascimento = models.DateTimeField(blank=True, null=True)
    SEXO_CHOICES = [('M', 'Masculino'), ('F', 'Feminino'), ('O', 'Outro')]
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, blank=True, null=True)

    def __str__(self):
        return self.nome


class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)
    email = models.EmailField(max_length=100)
    cargo = models.CharField(max_length=50, blank=True, null=True)
    salario = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    data_contratacao = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.nome} - {self.cargo or 'Funcionário'}"


class Operador(models.Model):
    nome_operador = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    senha = models.CharField(max_length=100)
    tipo_operador = models.CharField(max_length=50)

    def __str__(self):
        return self.nome_operador


class Servico(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    duracao = models.IntegerField(blank=True, null=True)  # Duração em minutos

    def __str__(self):
        return self.nome


class ServicoPrestado(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE)
    data_servico = models.DateTimeField()
    valor_cobrado = models.DecimalField(max_digits=10, decimal_places=2)
    observacoes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.servico.nome} para {self.cliente.nome}"


class Pagamento(models.Model):
    servico_prestado = models.ForeignKey(ServicoPrestado, on_delete=models.CASCADE)
    valor_pago = models.DecimalField(max_digits=10, decimal_places=2)
    data_pagamento = models.DateTimeField()
    metodo_pagamento = models.CharField(max_length=50)
    status = models.CharField(max_length=50)

    def __str__(self):
        return f"Pagamento de {self.valor_pago} - {self.status}"


class Despesa(models.Model):
    tipo_despesa = models.CharField(max_length=50)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.TextField(blank=True, null=True)
    data_despesa = models.DateTimeField()
    categoria = models.CharField(max_length=50, blank=True, null=True)
    operador = models.ForeignKey(Operador, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f"{self.tipo_despesa} - {self.valor}"


class FluxoCaixa(models.Model):
    tipo_operacao = models.CharField(max_length=50)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.TextField()
    data_operacao = models.DateTimeField()
    pagamento = models.ForeignKey(Pagamento, on_delete=models.SET_NULL, blank=True, null=True)
    operador = models.ForeignKey(Operador, on_delete=models.SET_NULL, blank=True, null=True)
    status = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.tipo_operacao} - {self.valor}"


class Operacao(models.Model):
    operador = models.ForeignKey(Operador, on_delete=models.CASCADE)
    tipo_operacao = models.CharField(max_length=50)
    descricao = models.TextField()
    data_operacao = models.DateTimeField(auto_now_add=True)
    fluxo = models.ForeignKey(FluxoCaixa, on_delete=models.SET_NULL, blank=True, null=True)
    status = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.tipo_operacao} - {self.status}"


class Salario(models.Model):
    funcionario = models.ForeignKey(Funcionario,  related_name='salarios', on_delete=models.CASCADE)
    valor_salario = models.DecimalField(max_digits=10, decimal_places=2)
    data_pagamento = models.DateField()
    observacoes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Salário de {self.funcionario.nome} - {self.valor}"
