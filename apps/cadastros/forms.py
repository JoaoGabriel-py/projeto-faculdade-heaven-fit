from django.forms import DecimalField, ModelForm
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
    valor = DecimalField(localize=True)
    
    class Meta:
        model = Modalidade
        fields = ['nome', 'descricao', 'professor', 'valor', 'status']
        
    def clean_valor(self):
        valor = self.cleaned_data.get('valor')
        if isinstance(valor, str):
            valor = valor.replace(',', '.')
        return valor
