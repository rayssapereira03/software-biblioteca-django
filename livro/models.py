from django.db import models
import datetime
from usuarios.models import Usuario

class Categoria(models.Model):
  titulo = models.CharField(max_length = 30)
  descricao = models.TextField()

  def __str__(self) -> str:
    return self.titulo

class Livros(models.Model):
  img = models.ImageField(upload_to='capa_livro', null = True, blank = True)
  titulo = models.CharField(max_length = 100)
  autor = models.CharField(max_length = 30)
  editora = models.CharField(max_length = 50)
  status = models.CharField(max_length = 8)
  #categoria = models.CharField(max_length = 100)
  emprestado = models.BooleanField(default = False)
  categoria = models.ForeignKey(Categoria, on_delete= models.DO_NOTHING)
  #codigo = models.CharField(max_length = 100)
  anoPublicacao = models.CharField(max_length = 4)
  #usuario = models.ForeignKey(Usuario, on_delete= models.DO_NOTHING)

  class Meta:
    verbose_name = 'Livro'
  
  def __str__(self):
    return f"{self.titulo} | {self.autor} | {self.editora} "

class Emprestimo(models.Model):
  nome_emprestado = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)
  data_emprestimo = models.DateTimeField(default = datetime.datetime.now())
  data_devolucao = models.DateTimeField(blank=True, null=True)
  data_prevista_devolucao = models.DateField(blank=True, null=True)
  cpf_biblio = models.CharField(max_length=11)
  livro = models.ForeignKey(Livros, on_delete=models.DO_NOTHING)
  
  class Meta:
    verbose_name = 'Emprestimo'
    
  def __str__(self):
    return f"{self.nome_emprestado} | {self.livro}"
