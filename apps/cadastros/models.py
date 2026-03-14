from django.db import models


class Aluno(models.Model):
    
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=14, unique=True)
    telefone = models.CharField(max_length=20)
    email = models.EmailField(max_length=255)
    data_matricula = models.DateField(auto_now_add=True)
    status = models.BooleanField(verbose_name='status_aluno', default=True)
    
    def __str__(self):
        return self.nome
    
    class Meta:
        ordering = ["nome"]
