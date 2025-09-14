from django.shortcuts import get_object_or_404, render, redirect
from .models import Livro, Estudante
from django.http import JsonResponse
import requests
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
         livro_emprestado_id = request.POST.get('livro_emprestado')
         livro_emprestado_obj = Livro.objects.get(id=livro_emprestado_id) if livro_emprestado_id else None
         estudante = Estudante(
                nome=nome,
                email=email,
                dataDeNascimento=dataDeNascimento,
                telefone=telefone,
                livro_emprestado=livro_emprestado_obj
        )

         estudante.save()
         return redirect('cadastrar_estudante')

def deletar_estudante(request, id): 
    estudante = get_object_or_404(Estudante, id=id)
    estudante.delete()
    return redirect('listar_estudantes')

def atualizar_estudante(request, id):
    estudante = get_object_or_404(Estudante, id=id)
    
    nome = request.POST.get('nome')
    email = request.POST.get('email')
    dataDeNascimento = request.POST.get('dataDeNascimento')
    telefone = request.POST.get('telefone')

    estudante.nome = nome
    estudante.email = email
    estudante.dataDeNascimento = dataDeNascimento
    estudante.telefone = telefone
    estudante.save()

    return redirect('listar_estudantes')

def listar_estudantes(request):
    estudantes = Estudante.objects.all()
    return render(request, 'app_biblioteca/estudantes/listar_estudantes.html', {'estudantes': estudantes})

def buscar_livro_openlibrary(request):
    isbn = request.GET.get('isbn')
    if not isbn:
        return JsonResponse({'erro': 'ISBN não informado'}, status=400)
    url = f'https://openlibrary.org/isbn/{isbn}.json'
    response = requests.get(url)
    print("Status:", response.status_code)
    print("Conteúdo:", response.text)
    if response.status_code == 200:
        data = response.json()
        autor_nomes= []
        for author in data.get('authors', []):
            author_key = author.get('key')
            if author_key:
                author_url = f'https://openlibrary.org{author_key}.json'
                author_resp = requests.get(author_url)
                if author_resp.status_code == 200:
                    author_data = author_resp.json()
                    autor_nomes.append(author_data.get('name', ''))
        livro_dados = {
            'titulo': data.get('title', ''),
            'autor': ', '.join(autor_nomes),
            'isbn': isbn,
            'editora': data.get('publishers', [''])[0],
            'assunto': data.get('description', ''),
            'paginas': data.get('number_of_pages', ''),
        }
        return JsonResponse(livro_dados)
    else:
        return JsonResponse({'erro': 'Livro não encontrado na biblioteca'}, status=404)