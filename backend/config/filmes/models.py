from django.db import models


class Filme(models.Model):
    titulo = models.CharField(max_length=255)
    diretor = models.CharField(max_length=255, blank=True)
    ano = models.PositiveIntegerField(null=True, blank=True)
    genero = models.CharField(max_length=100, blank=True)
    nota = models.PositiveSmallIntegerField(help_text="Nota de 1 a 10")
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.titulo} ({self.nota}/10)"
