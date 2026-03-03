from django.shortcuts import render, redirect, get_object_or_404
from .models import Aluno
from .forms import AlunoForm


def aluno_list(request):
    alunos = Aluno.objects.all()
    return render(request, 'cadastros/aluno_list.html', {'alunos': alunos})


def aluno_create(request):
    form = AlunoForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect('aluno_list')
    return render(request, 'cadastros/aluno_form.html', {'form': form})


def aluno_update(request, pk):
    aluno = get_object_or_404(Aluno, pk=pk)
    form = AlunoForm(request.POST or None, instance=aluno)
    
    if form.is_valid():
        form.save()
        return redirect('aluno_list')
    return render(request, 'cadastros/aluno_form.html', {'form': form})


def aluno_delete(request, pk):
    aluno = get_object_or_404(Aluno, pk=pk)
    
    if request.method == 'POST':
        aluno.delete()
        return redirect('aluno_list')
    
    return render(request, 'cadastros/aluno_confirm_delete.html', {'aluno': aluno})
