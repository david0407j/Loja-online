from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model




class Categoria(models.Model):
    nome = models.CharField(max_length=32,unique=True)

    def __str__(self):
        return f'{self.nome}'


class Produto(models.Model):
  
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=128)
    slug = models.SlugField(max_length=512)
    valor = models.CharField(max_length=32)
    criado_em = models.DateTimeField(auto_now_add=True)
    imagem = models.ImageField(upload_to='img/')
    featured = models.BooleanField(default = False)
    active  = models.BooleanField(default = True)

    def __str__(self):
        return f'{self.descricao}'

    def get_absolute_url(self):
        return reverse('produto:categoria', args=(self.slug,))


class Carrinho(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    produtos = models.ManyToManyField(Produto, through='CarrinhoItem')

    def __str__(self):
        produtos = [item.descricao for item in self.produtos.all()]
        return f'{self.user.id}: ({produtos})'



class CarrinhoItem(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    carrinho = models.ForeignKey(Carrinho, on_delete=models.CASCADE)
    quantidade = models.IntegerField(default=1)



