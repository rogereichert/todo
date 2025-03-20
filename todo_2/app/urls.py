from django.urls import path
from .views import cadastrar_tarefa

urlpatterns = [
    path('cadastrar_tarefa/', cadastrar_tarefa, name='cadastrar_tarefa')
]