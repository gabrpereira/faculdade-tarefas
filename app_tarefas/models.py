from django.db import models

class Tarefa(models.Model):
    # Título da tarefa (texto)
    titulo = models.CharField(max_length=200)
    # Status (verdadeiro/falso) - começa como falso
    concluida = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo