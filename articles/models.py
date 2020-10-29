from django.db import models
from django.utils import timezone
import datetime

class Article(models.Model):
    article_title = models.CharField('название статьи',max_length=200)
    article_text = models.TextField('текст статьи')
    pub_date = models.DateTimeField('дата публикации')

    def __str__(self):
        return self.article_title

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=3)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class Coment(models.Model):
    articles = models.ForeignKey(Article, on_delete=models.CASCADE)
    coment_autor = models.CharField('имя автора', max_length=50)
    coment_text = models.CharField('текст коментария', max_length=200)

    def __str__(self):
        return self.coment_text

    class Meta:
        verbose_name = 'Коментарий'
        verbose_name_plural = 'Коментарии'