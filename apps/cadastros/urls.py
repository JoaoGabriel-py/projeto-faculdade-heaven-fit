from django.urls import path
from .views import aluno_list, aluno_create, aluno_update, aluno_delete

urlpatterns = [
    path('', aluno_list, name='aluno_list'),
    path('criar-aluno', aluno_create, name='aluno_create'),
    path('atualizar-aluno/<int:pk>/', aluno_update, name='aluno_update'),
    path('deletar-aluno/<int:pk>/', aluno_delete, name='aluno_delete'),
]
