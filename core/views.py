from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse

from .forms import ContatoForm,ProdutoModelForm
from .models import  Produto


def index(request):
    context = {
        'produtos' : Produto.objects.all()
    }

    return render(request, 'index.html',context)


def contato(request):
    formulario = ContatoForm(request.POST or None)

    if str(request.method) == 'POST':
        if formulario.is_valid():
            formulario.send_email()

            messages.success(request, 'E-mail foi enviado com sucesso')
            formulario = ContatoForm()
        else :
            messages.error(request, 'Erro ao enviar e-mail')

    context = {
        'form': formulario
    }

    return render(request, 'contato.html', context)


def produto(request):
    # só irá renderizar caso o Usuário não for anonymous, ou seja algum usuário deve estar logar para funcionar
    if str(request.user) != 'AnonymousUser':
        usuario = str(request.user)
        if str(request.method) == 'POST':
            form = ProdutoModelForm(request.POST, request.FILES)
            if form.is_valid():
                # caso o formulário for valido, form.save() irá salvar os dados no banco de dados
                form.save()

                messages.success(request,'Produto salvo com sucesso.')
                form = ProdutoModelForm()
            else :
                messages.error(request, 'Erro ao salvar o produto.')
        else :
            form = ProdutoModelForm()
        context = {
            'formulario': form,
            'usuario': usuario
        }
        return render(request, 'produto.html',context)
    else :

        return redirect('index')

