from django.db import models
from django.conf import settings
from django.utils.text import slugify
from PIL import Image
import os
from utils.utils import formata_preco
# Create your models here.

class Produto(models.Model):
    nome = models.CharField(max_length=255)
    descricao_curta  = models.TextField(max_length=255)
    descricao_longa  = models.TextField()
    imagem  = models.ImageField(upload_to='produto/%Y/%m/', blank=True, null=True)
    slug  = models.SlugField(unique=True, blank=True, null=True)
    preco_marketing  = models.FloatField()
    preco_marketing_promocional  = models.FloatField(default=0)
    tipo  = models.CharField(default='variável', max_length=1, choices=(('V', 'Variável'),
                                                                         ('S', 'Simples' )))
    
    def get_preco_formatado(self):
        return formata_preco(self.preco_marketing)
    get_preco_formatado.short_description = 'Preço'
    

    def get_preco_promo_formatado(self):
        return formata_preco(self.preco_marketing_promocional)
    get_preco_promo_formatado.short_description = 'Preço Promo'


    @staticmethod
    def resize_image(img, new_width=800):
        img_full_path = os.path.join(settings.MEDIA_ROOT, img.name)
        img_pill = Image.open(img_full_path)
        original_width, original_height = img_pill.size
        

        if original_width <= new_width:
            img_pill.close()
            return 
        
        new_height = round((new_width * original_height) / original_width)
        new_img = img_pill.resize((new_width, new_height), Image.LANCZOS)
        new_img.save(
            img_full_path,
            optimize=True,
            quality=50
        )
        print('A imagem foi redimensionada')


    def save(self, *args, **kwargs):
        if not self.slug:
            slug = f'{slugify(self.nome)}'
            self.slug = slug

        super().save(*args, **kwargs)
        max_image_size = 800
        if self.imagem:



            self.resize_image(self.imagem, max_image_size)
    def __str__(self):
        return self.nome
    

class Variacao(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    nome = models.CharField(max_length=255, blank=True, null=True)
    preco = models.FloatField()
    preco_promocional = models.FloatField(default=0)
    estoque = models.PositiveIntegerField(default=1)
    

    def __str__(self):
        return self.nome or self.Produto.nome
    class Meta:
        verbose_name = "Variação"
        verbose_name_plural = "Variações"
        