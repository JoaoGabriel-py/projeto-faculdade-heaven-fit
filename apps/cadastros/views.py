from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from .models import Aluno, Matricula, Modalidade, Presenca
from .forms import (
    AlunoCreateForm,
    AlunoUpdateForm,
    ModalidadeCreateForm,
    ModalidadeUpdateForm,
)
from .forms import (
    MatriculaCreateForm,
    MatriculaUpdateForm,
    PresencaCreateForm,
    PresencaUpdateForm,
)


def aluno_list(request):
    alunos = Aluno.objects.filter(status=True)

    paginator = Paginator(alunos, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "aluno/aluno_list.html", {"alunos": page_obj})


def aluno_create(request):
    form = AlunoCreateForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("aluno_list")

    return render(request, "aluno/aluno_create.html", {"form": form})


def aluno_update(request, pk):
    aluno = get_object_or_404(Aluno, pk=pk)
    form = AlunoUpdateForm(request.POST or None, instance=aluno)

    if form.is_valid():
        form.save()
        return redirect("aluno_list")

    return render(request, "aluno/aluno_update.html", {"aluno": form})


def aluno_delete(request, pk):
    aluno = get_object_or_404(Aluno, pk=pk)

    if request.method == "POST":
        aluno.status = False
        aluno.save()

    return redirect(request.META.get("HTTP_REFERER", "aluno_list"))


def modalidade_list(request):
    modalidades = Modalidade.objects.filter(status=True)

    paginator = Paginator(modalidades, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "modalidade/modalidade_list.html", {"modalidades": page_obj})


def modalidade_create(request):
    form = ModalidadeCreateForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("modalidade_list")

    return render(request, "modalidade/modalidade_create.html", {"form": form})


def modalidade_update(request, pk):
    modalidade = get_object_or_404(Modalidade, pk=pk)
    form = ModalidadeUpdateForm(request.POST or None, instance=modalidade)

    if form.is_valid():
        form.save()
        return redirect("modalidade_list")

    return render(request, "modalidade/modalidade_update.html", {"modalidade": form})


def modalidade_delete(request, pk):
    modalidade = get_object_or_404(Modalidade, pk=pk)

    if request.method == "POST":
        modalidade.status = False
        modalidade.save()

    return redirect(request.META.get("HTTP_REFERER", "modalidade_list"))


def matricula_list(request):
    matriculas = Matricula.objects.filter()

    paginator = Paginator(matriculas, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "matricula/matricula_list.html", {"matriculas": page_obj})


def matricula_create(request):
    form = MatriculaCreateForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("matricula_list")

    alunos = Aluno.objects.filter(status=True)
    modalidades = Modalidade.objects.filter(status=True)

    return render(
        request,
        "matricula/matricula_create.html",
        {
            "form": form,
            "alunos": alunos,
            "modalidades": modalidades,
        },
    )


def matricula_update(request, pk):
    matricula = get_object_or_404(Matricula, pk=pk)
    form = MatriculaUpdateForm(request.POST or None, instance=matricula)

    if form.is_valid():
        form.save()
        return redirect("matricula_list")

    alunos = Aluno.objects.filter(status=True)
    modalidades = Modalidade.objects.filter(status=True)

    return render(
        request,
        "matricula/matricula_update.html",
        {
            "matricula": form,
            "alunos": alunos,
            "modalidades": modalidades,
        },
    )


def matricula_delete(request, pk):
    matricula = get_object_or_404(Matricula, pk=pk)

    if request.method == "POST":
        matricula.status = False
        matricula.save()

    return redirect(request.META.get("HTTP_REFERER", "matricula_list"))


def presenca_list(request):
    presencas = Presenca.objects.filter(status=True)

    paginator = Paginator(presencas, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "presenca/presenca_list.html", {"presencas": page_obj})


def presenca_create(request):
    form = PresencaCreateForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("presenca_list")

    matriculas = Matricula.objects.filter(status=True)

    return render(
        request,
        "presenca/presenca_create.html",
        {
            "form": form,
            "matriculas": matriculas,
        },
    )


def presenca_update(request, pk):
    presenca = get_object_or_404(Presenca, pk=pk)
    form = PresencaUpdateForm(request.POST or None, instance=presenca)

    if form.is_valid():
        form.save()
        return redirect("presenca_list")

    matriculas = Matricula.objects.filter(status=True)

    return render(
        request,
        "presenca/presenca_update.html",
        {"presenca": form, "matriculas": matriculas},
    )


def presenca_delete(request, pk):
    presenca = get_object_or_404(Presenca, pk=pk)

    if request.method == "POST":
        presenca.status = False
        presenca.save()

    return redirect(request.META.get("HTTP_REFERER", "presenca_list"))
