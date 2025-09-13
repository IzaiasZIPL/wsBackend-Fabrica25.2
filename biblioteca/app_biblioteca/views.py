from django.shortcuts import render, redirect
from .models import Livro, Estudante
#from .forms import PessoaForm

def home(request):
    return render(request, 'home.html')

