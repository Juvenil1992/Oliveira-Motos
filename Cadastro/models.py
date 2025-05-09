from django.db import models

# Create your models here.

class Cad_Passeios(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    destino = models.CharField(max_length=100)
    localPartida = models.CharField(max_length=100)
    horarioPartida = models.CharField(max_length=5) 
    grupoWhats = models.CharField(max_length=100)
    DataPasseio = models.CharField(max_length=10, null=True, blank=True)
    
    def __str__(self):
        return self.nome