from django.urls import path
from .views import aluno_list, aluno_create, aluno_update, aluno_delete
from .views import modalidade_list, modalidade_create, modalidade_update, modalidade_delete

urlpatterns = [
    path('', aluno_list, name='aluno_list'),
    path('criar-aluno', aluno_create, name='aluno_create'),
    path('atualizar-aluno/<int:pk>/', aluno_update, name='aluno_update'),
    path('deletar-aluno/<int:pk>/', aluno_delete, name='aluno_delete'),
    path('modalidades/', modalidade_list, name='modalidade_list'),
    path('criar-modalidade/', modalidade_create, name='modalidade_create'),
    path('atualizar-modalidade/<int:pk>/', modalidade_update, name='modalidade_update'),
    path('deletar-modalidade/<int:pk>/', modalidade_delete, name='modalidade_delete'),
]
