from django.db import models # type: ignore
from stdimage.models import StdImageField # type: ignore

# SIGNALS - 
from django.db.models import signals # type: ignore sinal para realizar operação antes do models ir para o DB
from django.template.defaultfilters import slugify # type: ignore
# titulo/coisa separado por traços para criar url valida

class Base(models.Model): # abstrata - n criada em DB - é um rascunho para outras
    criado = models.DateField('Data de criação', auto_now_add=True)
    modificado = models.DateField('Data de atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)
    class Meta:
        abstract = True

class Produto(Base):
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField('Preço', max_digits=8, decimal_places=2)
    estoque = models.IntegerField('Estoque', default=0)
    img = StdImageField('Imagem', upload_to='produtos', variations={'thumb': (124, 124)})
    slug = models.SlugField('Slug', max_length=100, blank=True, editable=False)
    def __str__(self):
        return self.nome

# criando signals
"""
antes de salvar... execute a função quando Produto enviar o sinal
"""
def produto_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.nome)

signals.pre_save.connect(produto_pre_save, sender=Produto)


