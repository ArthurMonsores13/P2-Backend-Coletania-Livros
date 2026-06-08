from django.shortcuts import render, get_object_or_404, redirect
from .models import Filme
from .forms import FilmeForm


def cadastrar(request):
    if request.method == "POST":
        form = FilmeForm(request.POST)
        if form.is_valid():
            filme = form.save()
            return redirect("detalhe", pk=filme.pk)
    else:
        form = FilmeForm()
    return render(request, "filmes/cadastrar.html", {"form": form})


def detalhe(request, pk):
    filme = get_object_or_404(Filme, pk=pk)
    return render(request, "filmes/detalhe.html", {"filme": filme})


def editar(request, pk):
    filme = get_object_or_404(Filme, pk=pk)
    if request.method == "POST":
        form = FilmeForm(request.POST, instance=filme)
        if form.is_valid():
            form.save()
            return redirect("detalhe", pk=filme.pk)
    else:
        form = FilmeForm(instance=filme)
    return render(request, "filmes/editar.html", {"form": form, "filme": filme})


def excluir(request, pk):
    filme = get_object_or_404(Filme, pk=pk)
    if request.method == "POST":
        filme.delete()
        return redirect("buscar")
    return render(request, "filmes/excluir.html", {"filme": filme})


def listar(request):
    filmes = Filme.objects.all().order_by("-criado_em")
    return render(request, "filmes/listar.html", {"filmes": filmes})


def buscar(request):
    nome = request.GET.get("q", "").strip()
    filmes = Filme.objects.filter(titulo__icontains=nome) if nome else []
    return render(request, "filmes/buscar.html", {"filmes": filmes, "query": nome})
