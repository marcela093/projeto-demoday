from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
class Depoimento(models.Model):
    empresa = models.CharField(max_length=200)
    funcionaria_atual = models.BooleanField
    avaliacao = models.TextField()
    recomendacao = models.CharField(max_length=200)
    data = models.DateTimeField(default=timezone.now)

    def publicar(self):
        self.data = timezone.now()
        self.save()

    def __str__(self):
        return self.avaliacao    

class Usuario(models.Model):
    nome = models.CharField(max_length=200)
    sobrenome = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    senha = models.CharField(max_length=200)