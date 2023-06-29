from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    periodo_ingresso = models.CharField(max_length=10)
    nota_web_avancado = models.DecimalField(max_digits=3, decimal_places=1)
    situacao = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
