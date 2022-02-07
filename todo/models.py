from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
    title = models.CharField('Название', max_length=100)
    memo = models.TextField('Описание', blank=True)
    created = models.DateTimeField('Дата создания', auto_now_add=True)
    datecompleted = models.DateTimeField('Дата завершения', null=True, blank=True)
    important = models.BooleanField('Важно', default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title