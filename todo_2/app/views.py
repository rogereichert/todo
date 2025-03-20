from django.shortcuts import render

# Create your views here.
def cadastrar_tarefa(request):
    return render(request, 'form_cadastro.html')