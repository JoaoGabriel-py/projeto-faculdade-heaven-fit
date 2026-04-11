from django.forms import ModelForm
from .models import Aluno, Modalidade


class AlunoCreateForm(ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome', 'cpf', 'telefone', 'email']
        

class AlunoUpdateForm(ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome', 'cpf', 'telefone', 'email', 'status']
        

class ModalidadeCreateForm(ModelForm):
    class Meta:
        model = Modalidade
        fields = ['nome', 'descricao', 'professor', 'valor']
        

class ModalidadeUpdateForm(ModelForm):
    class Meta:
        model = Modalidade
        fields = ['nome', 'descricao', 'professor', 'valor', 'status']
