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


class Modalidade(models.Model):
    
    nome = models.CharField(max_length=255, blank=False, null=False)
    descricao = models.TextField(blank=True, null=True)
    professor = models.CharField(max_length=255, blank=False, null=False)
    valor = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    status = models.BooleanField(default=True)
    
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nome
    
    class Meta:
        ordering = ["nome"]


class Matricula(models.Model):
    
    aluno = models.ForeignKey(
        'Aluno',
        on_delete=models.CASCADE,
        related_name='matriculas'
    )
    
    modalidade = models.ForeignKey(
        'Modalidade',
        on_delete=models.CASCADE,
        related_name='matriculas'
    )
    
    data_matricula = models.DateField(auto_now_add=True)
    
    status = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.aluno.nome} - {self.modalidade.nome}"
    
    class Meta:
        ordering = ["data_matricula"]
        unique_together = ('aluno', 'modalidade')
