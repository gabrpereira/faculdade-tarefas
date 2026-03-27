from django.shortcuts import render, redirect
from .models import Tarefa

def lista_tarefas(request):
    if request.method == 'POST':
        texto_digitado = request.POST.get('novo_titulo')
        if texto_digitado: # Uma boa prática: só cria se não estiver vazio
            Tarefa.objects.create(titulo=texto_digitado)
        return redirect('home')
        
    minhas_tarefas = Tarefa.objects.all()
    return render(request, 'lista.html', {'tarefas': minhas_tarefas})

def concluir_tarefa(request, tarefa_id):
    tarefa = Tarefa.objects.get(id=tarefa_id)
    tarefa.concluida = True
    tarefa.save()
    return redirect('home')

def deletar_tarefa(request, tarefa_id):
    tarefa = Tarefa.objects.get(id=tarefa_id)
    # CORREÇÃO AQUI: .delete() é uma função que remove do banco
    tarefa.delete() 
    return redirect('home')