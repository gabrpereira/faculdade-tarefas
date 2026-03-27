from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_tarefas, name='home'),
    # <int:tarefa_id> captura o número da tarefa e passa para a view
    path('concluir/<int:tarefa_id>/', views.concluir_tarefa, name='concluir'),
    path('deletar/<int:tarefa_id>/', views.deletar_tarefa, name='deletar'),
]