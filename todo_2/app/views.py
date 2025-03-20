from django.shortcuts import render
from .forms import TarefaForm

# Create your views here.
def cadastrar_tarefa(request):
    form_tarefa = TarefaForm()
    return render(request, 'form_cadastro.html', {'form_tarefa': form_tarefa})