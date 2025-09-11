from django.db import models

class Cep(models.Model):
    cep = models.CharField(max_length=9, unique=True)
    logradouro = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)

    def __str__(self):
        return self.cep
