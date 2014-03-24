from django.db import models

class Pagina(models.Model):
    nome = models.CharField(max_length='20', primary_key=True)
    conteudo = models.TextField(blank=True)