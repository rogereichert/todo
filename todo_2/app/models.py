from django.db import models

class Tarefa(models.Model):
    
    STATUS_CHOICES = (
        (1, 'A fazer'),
        (2, 'Fazendo'),
        (3, 'Concluído')
    )
    
    titulo = models.CharField(max_length=100, blank=False, null=False)
    descricao = models.TextField(blank=False, null=False)
    data = models.DateField(null=False, blank=False)
    status = models.IntegerField(choices=STATUS_CHOICES, null=False, blank=False)
    