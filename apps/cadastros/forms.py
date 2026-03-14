from django.forms import ModelForm
from .models import Aluno


class AlunoCreateForm(ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome', 'cpf', 'telefone', 'email']
        

class AlunoUpdateForm(ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome', 'cpf', 'telefone', 'email', 'status']
