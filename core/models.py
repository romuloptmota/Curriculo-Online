from django.db import models


class Base(models.Model):
    criados = models.DateField('Criação', auto_now_add=True)
    modificado = models.DateField('Atualização', auto_now=True)

    class Meta:
        abstract = True


class Inicio(Base):
    nome = models.CharField('Nome', max_length=100)
    profissao1 = models.CharField('Profissção 1', max_length=100)
    profissao2 = models.CharField('Profissão 2', max_length=100)
    github = models.CharField('GitHub', max_length=100, default='#')
    linkedin = models.CharField('Linkedin', max_length=100, default='#')
    facebook = models.CharField('Facebook', max_length=100, default='#')
    descricao = models.TextField('Descrição', max_length=200)
    nacionalidade = models.CharField('Nacionalidade', max_length=100)
    cidade_estado = models.CharField('Cidade, Estado', max_length=100)
    email = models.CharField('E-mail', max_length=100)
    telefone = models.CharField('Telefone', max_length=100)

    def __str__(self):
        return self.nome
