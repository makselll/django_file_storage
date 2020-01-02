from django.db import models
from django.contrib.auth.models import User


class Document(models.Model):
    title = models.CharField('Название документа', max_length=200)
    user = models.ForeignKey(User, on_delete= models.CASCADE, related_name='doc_user')
    file = models.FileField('Файл', upload_to="documents")
    description = models.CharField('Краткое описание', max_length=400)
    private = models.BooleanField('Приватный ?', null= True)
    score = models.IntegerField('рейтинг', null= True,default=0)

    def view_count(self):

        return sum([i.value for i in PostLikes.objects.filter(document=self)])

    class Meta:
        verbose_name= ':Документы'
        verbose_name_plural = 'Документ'

    def __str__(self):
        return self.title


class PostLikes(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE, related_name='like_user')
    document = models.ForeignKey(Document, on_delete= models.CASCADE)
    value = models.IntegerField(verbose_name='-1/1', null = True)