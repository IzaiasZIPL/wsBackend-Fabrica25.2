from . import views
from django.urls import path
from .views import listar_livros, cadastrar_livro, deletar_livro, atualizar_livro, listar_estudantes, cadastrar_estudante, deletar_estudante, atualizar_estudante, home

#rota, view e nome de referencia
urlpatterns = [
    path('home/', home, name='home'),
    path('listar_livros/', listar_livros, name= 'listar_livros'),
    path('cadastrar_livro/', cadastrar_livro, name= 'cadastrar_livro'),
    path('deletar_livro/<int:id>', deletar_livro, name = 'deletar_livro'),
    path('atualizar_livro/<int:id>', atualizar_livro, name = 'atualizar_livro'),
    path('listar_estudantes/', listar_estudantes, name='listar_estudantes'),
    path('cadastrar_estudante/', cadastrar_estudante, name='cadastrar_estudante'),
    path('deletar_estudante/<int:id>', deletar_estudante, name='deletar_estudante'),
    path('atualizar_estudante/<int:id>', atualizar_estudante, name='atualizar_estudante'),
    path('buscar_livro/', views.buscar_livro_openlibrary, name='buscar_livro'),
    ]