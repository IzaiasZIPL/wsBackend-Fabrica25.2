from django.urls import path
from . import views
from .views import listar_livros, criar_livro, listar_estudantes, criar_estudante

#rota, view e nome de referencia
urlpatterns = [
    path('', views.home, name='home'),
    path('listar_livros/', listar_livros, name= 'listar_livros'),
    path('criar_livro/', criar_livro, name= 'criar_livro'),
    path('listar_estudantes/', listar_estudantes, name='listar_estudantes'),
    path('criar_estudante/', criar_estudante, name='criar_estudante'),
    ]