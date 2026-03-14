from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from .models import Aluno
from .forms import AlunoForm


def aluno_list(request):
    alunos = Aluno.objects.all()
    
    paginator = Paginator(alunos, 10)  # 10 alunos por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'aluno_list.html', {'alunos': page_obj})


def aluno_create(request):
    form = AlunoForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect('aluno_list')
    
    return render(request, 'aluno_create.html', {'form': form})


def aluno_update(request, pk):
    aluno = get_object_or_404(Aluno, pk=pk)
    form = AlunoForm(request.POST or None, instance=aluno)
    
    if form.is_valid():
        form.save()
        return redirect('aluno_list')
    
    return render(request, 'aluno_update.html', {'aluno': form})


def aluno_delete(request, pk):
    aluno = get_object_or_404(Aluno, pk=pk)
    
    if request.method == 'POST':
        aluno.delete()
        return redirect('aluno_list')
    
    return render(request, 'aluno_confirm_delete.html', {'aluno': aluno})
