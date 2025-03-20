from django.shortcuts import render
from .forms import TarefaForm

# Create your views here.
def cadastrar_tarefa(request):
    if request.method == 'POST':
        form_tarefa = TarefaForm(request.POST)
        if form_tarefa.is_valid():
            form_tarefa.save()
    else:
        form_tarefa = TarefaForm()
    return render(request, 'form_cadastro.html', {'form_tarefa': form_tarefa})