from django.urls import path
from . import views
from .views import listar_livros, cadastrar_livro, deletar_livro, atualizar_livro#, listar_estudantes, cadastrar_estudante

#rota, view e nome de referencia
urlpatterns = [
    path('', views.home, name='home'),
    path('listar_livros/', listar_livros, name= 'listar_livros'),
    path('cadastrar_livro/', cadastrar_livro, name= 'cadastrar_livro'),
    path('deletar_livro/<int:id>', deletar_livro, name = 'deletar_livro'),
    path('atualizar_livro/<int:id>', atualizar_livro, name = 'atualizar_livro'),
    #path('listar_estudantes/', listar_estudantes, name='listar_estudantes'),
    #path('cadastrar_estudante/', cadastrar_estudante, name='cadastrar_estudante'),
    ]