from django.shortcuts import get_object_or_404, render, redirect
from .models import Livro, Estudante
#from .forms import PessoaForm

def home(request):
    return render(request, 'home.html')
#viws de livros
def cadastrar_livro(request):
  if request.method == 'GET':
    return render(request, 'app_biblioteca/livros/cadastrar_livros.html')
  elif request.method == 'POST':
     titulo = request.POST.get('titulo')
     autor = request.POST.get('autor')
     isbn = request.POST.get('isbn')
     editora = request.POST.get('editora')
     assunto = request.POST.get('assunto')
     paginas = request.POST.get('paginas')

     livro = Livro(
        titulo=titulo, 
        autor=autor, 
        isbn=isbn, 
        editora=editora, 
        assunto=assunto, 
        paginas=paginas
    )
     
     livro.save()
     return redirect('cadastrar_livro')
  
def deletar_livro(request, id): 
    livro = get_object_or_404(Livro, id=id)
    livro.delete()
    return redirect('listar_livros')

def atualizar_livro(request, id): 
    livro = get_object_or_404(Livro, id=id)
    
    titulo = request.POST.get('titulo')
    autor = request.POST.get('autor')
    isbn = request.POST.get('isbn')
    editora = request.POST.get('editora')
    assunto = request.POST.get('assunto')
    paginas = request.POST.get('paginas')

    livro.titulo = titulo
    livro.autor = autor
    livro.isbn = isbn
    livro.editora = editora
    livro.assunto = assunto
    livro.paginas = paginas
    livro.save()

    return redirect('listar_livros')

def listar_livros(request):
    livros = Livro.objects.all()
    return render(request, 'app_biblioteca/livros/listar_livros.html', {'livros': livros})

#views de estudantes

def cadastrar_estudante(request):
  if request.method == 'GET':
    return render(request, 'app_biblioteca/estudantes/cadastrar_estudantes.html')
  elif request.method == 'POST':
     nome = request.POST.get('nome')
     email = request.POST.get('email')
     dataDeNascimento = request.POST.get('dataDeNascimento')
     telefone = request.POST.get('telefone')

     estudante = Estudante(
        nome=nome,
        email=email,
        dataDeNascimento=dataDeNascimento,
        telefone=telefone
    )

     estudante.save()
     return redirect('cadastrar_estudante')

def deletar_estudante(request, id): 
    estudante = get_object_or_404(Estudante, id=id)
    estudante.delete()
    return redirect('listar_estudantes')


