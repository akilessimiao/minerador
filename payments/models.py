from django.db import models
from django.contrib.auth.models import User

class Ordem(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=10, decimal_places=2)

class Saldo(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2)

class Pagamento(models.Model):
    valor = models.DecimalField(max_digits=10, decimal_places=2)  # Valor do pagamento
    data = models.DateTimeField(auto_now_add=True)  # Data do pagamento (registrada automaticamente)
    descricao = models.CharField(max_length=255, blank=True)  # Descrição opcional do pagamento

    def __str__(self):
        return f"Pagamento de {self.valor} em {self.data}"

class Saldo(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    moeda = models.CharField(max_length=10)
    saldo = models.DecimalField(max_digits=18, decimal_places=8)
    
    def __str__(self):
        return f'{self.usuario.username} - {self.moeda} - {self.saldo}'
