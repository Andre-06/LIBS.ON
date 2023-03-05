from django.db import models
from posts.models import Book, User


class PurchaseOrder(models.Model):
    choice_status = [
        ('AG', 'Aguardando Aprovação'),
        ('AP', 'Aprovado'),
        ('RE', 'Recusado')
    ]

    book = models.ForeignKey(Book, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    status = models.CharField(max_length=2, choices=choice_status, default='AG')
    data = models.DateTimeField() 
