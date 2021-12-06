from django.db import models
from mdeditor.fields import MDTextField

TITLE_CHOICES = (
    ('danger', '重要'),
    ('warning', '連絡'),
    ('info', 'イベント'),
    ('success', 'その他'),
)

class TagModel(models.Model):
    name = models.CharField('タグ', max_length=200, unique=True)

    def __str__(self):
        return self.name

class ArticleModel(models.Model):
    name = models.CharField(max_length=70)
    title = models.CharField(max_length=100, choices=TITLE_CHOICES)
    tags = models.ManyToManyField(TagModel, verbose_name='タグ', blank=True)

    content = MDTextField()
    created_at = models.DateField(verbose_name='作成日', auto_now=True)

    def __str__(self):
        return self.title

class CommentModel(models.Model):
    name = models.CharField('名前', max_length=100, default='John Doe')
    comment = models.TextField('コメント')
    target = models.ForeignKey(ArticleModel, on_delete=models.CASCADE, verbose_name='対象記事')
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment[:15]