from email.policy import default
from django.db import models


class Post(models.Model):
    """Посты в разделе 'Мини Блог'"""
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    body = models.TextField(blank=True, default='')
    image = models.ImageField(upload_to='images/posts/', default='image')
    owner = models.ForeignKey(
        'auth.User', related_name='posts', on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['created']
        db_table = 'posts'

    def __str__(self) -> str:
        return self.title


class Comment(models.Model):
    """Комментарии клиентов"""
    created = models.DateTimeField(auto_now_add=True)
    body = models.TextField(blank=False)
    post = models.ForeignKey(
        'Post', related_name='comments', on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        ordering = ['created']
        db_table = 'comments'

    def __str__(self) -> str:
        return str(self.post)


class Category(models.Model):
    """Категория мини блога"""
    name = models.CharField(max_length=100, blank=True, default='')
    posts = models.ManyToManyField(
        'Post', related_name='categories', blank=True)
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        db_table = 'categoryes'

    def __str__(self) -> str:
        return self.name


class Service(models.Model):
    """Услуга"""
    title = models.CharField(max_length=100, default='')
    body = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'
        db_table = 'services'

    def __str__(self) -> str:
        return self.title


class Portfolio(models.Model):
    """Портфолио"""
    title = models.CharField(max_length=100, default='')
    body = models.TextField()
    image = models.ImageField(upload_to='images/portfolio/', default='image')

    class Meta:
        verbose_name = 'Portfolio'
        db_table = 'portfolio'

    def __str__(self) -> str:
        return self.title