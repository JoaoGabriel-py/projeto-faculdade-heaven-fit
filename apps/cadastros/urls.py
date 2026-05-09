from django.urls import path
from .views import aluno_list, aluno_create, aluno_update, aluno_delete
from .views import modalidade_list, modalidade_create, modalidade_update, modalidade_delete
from .views import matricula_list, matricula_create, matricula_update, matricula_delete

urlpatterns = [
    # Aluno
    path('', aluno_list, name='aluno_list'),
    path('criar-aluno', aluno_create, name='aluno_create'),
    path('atualizar-aluno/<int:pk>/', aluno_update, name='aluno_update'),
    path('deletar-aluno/<int:pk>/', aluno_delete, name='aluno_delete'),
    # Modalidade
    path('modalidades/', modalidade_list, name='modalidade_list'),
    path('criar-modalidade/', modalidade_create, name='modalidade_create'),
    path('atualizar-modalidade/<int:pk>/', modalidade_update, name='modalidade_update'),
    path('deletar-modalidade/<int:pk>/', modalidade_delete, name='modalidade_delete'),
    # Matricula
    path('matriculas/', matricula_list, name='matricula_list'),
    path('criar-matricula/', matricula_create, name='matricula_create'),
    path('atualizar-matricula/<int:pk>/', matricula_update, name='matricula_update'),
    path('deletar-matricula/<int:pk>/', matricula_delete, name='matricula_delete'),
]
