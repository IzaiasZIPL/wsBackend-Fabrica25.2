from django.db import models

# Create your models here.

class Livro(models.Model):
    titulo = models.CharField(max_length=100)
    isbn = models.IntegerField(unique=True)
    autor = models.CharField(max_length=50, default="Desconhecido")
    editora = models.CharField(max_length=30)
    assunto = models.CharField(max_length=50)
    paginas = models.IntegerField()


    def __str__(self):
        return self.titulo
    

class Estudante(models.Model):
    nome = models.CharField(max_length=100)
    dataDeNascimento = models.DateField()
    telefone = models.IntegerField()
    email = models.EmailField(max_length=50)
    


    def __str__(self):
        return self.nome