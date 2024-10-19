from django.db import models

# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=23, unique=True)

    def __str__(self):
        return self.nome


class Tag(models.Model):
    nome = models.CharField(max_length=23, unique=True)
    descricao = models.CharField(max_length=350, unique=True)

    def __str__(self):
        return self.nome
    
class Jogo(models.Model):
    nome = models.CharField(max_length=23)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    valor = models.DecimalField(decimal_places=2, max_digits=9)
    data_lancamento = models.DateField()
    foto_capa = models.ImageField(upload_to="jogos_capa", null=True)
    desenvolvedora = models.CharField(max_length=100, null=True)
    descricao = models.TextField()
    
# class Aluno(models.Model):
#     nome = models.CharField(max_length=10)
#     idade = models.IntegerField(default=0)
#     nota01 = models.DecimalField(default=0, decimal_places=2, max_digits=4)
#     nota02 = models.DecimalField(default=0, decimal_places=2, max_digits=4)
#     nota03 = models.DecimalField(default=0, decimal_places=2, max_digits=4)

# class Curso(models.Model):
#     nome = models.CharField(max_length=50)
#     duracao = models .IntegerField(default=0)

# class Turma(models.Model):
#     data_inicio = models.DateTimeField()
#     curso = models.ForeignKey(Curso, on_delete=models.CASCADE, blank=True, null=True)
