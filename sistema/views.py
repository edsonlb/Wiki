from django.shortcuts import render
from sistema.models import Pagina
import markdown


def mostrar_pagina(request, nomePagina):
    try:
        pagina = Pagina.objects.get(pk=nomePagina)
    except:
        return render(request, 'criarPagina.html', {'nomePagina': nomePagina})

    return render(request, 'mostraPagina.html', {'pagina': pagina})

def editar_pagina(request,nomePagina):
    try:
        pagina = Pagina.objects.get(pk=nomePagina)
    except:
        pagina = Pagina(nome=nomePagina)

    return render(request, 'editarPagina.html', {'pagina': pagina})

def salvar_pagina(request, nomePagina):
    conteudoNovo = markdown.markdown(request.POST.get('conteudo',''))
    try:
        pagina = Pagina.objects.get(pk = nomePagina)
        pagina.conteudo = conteudoNovo
    except:
        pagina = Pagina(nome=nomePagina, conteudo=conteudoNovo)

    pagina.save()
    return mostrar_pagina(request, pagina.nome)
