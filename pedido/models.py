from django.db import models

class Pedido(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.FloatField()
    status = models.CharField(
        default="C",
        max_length=1,
        choices= (
            ('A', 'Aprovado'),
            ('C', 'Aprovado'),
            ('R', 'Aprovado'),
            ('P', 'Aprovado'),
            ('E', 'Aprovado'),
            ('F', 'Aprovado'),
            ('A', 'Aprovado'),
            ('A', 'Aprovado'),
            ('A', 'Aprovado'),
            ('A', 'Aprovado'),
            ('A', 'Aprovado'),

        )
    )
class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    produto = models.CharField
