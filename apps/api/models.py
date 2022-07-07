from django.db import models


class Post(models.Model):
    created = models.DateTimeField(
        auto_now_add=True)
    title = models.CharField(
        max_length=100, blank=True, default='')
    body = models.TextField(
        blank=True, default='')
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
    created = models.DateTimeField(
        auto_now_add=True)
    body = models.TextField(
        blank=False)
    owner = models.ForeignKey(
        'auth.User', related_name='comments', on_delete=models.CASCADE)
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
    name = models.CharField(
        max_length=100, blank=True, default='')
    owner = models.ForeignKey(
        'auth.User', related_name='categories', on_delete=models.CASCADE)
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
    title = models.CharField(
        max_length=100, default='')
    body = models.TextField(
        blank=True)

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'
        db_table = 'services'

    def __str__(self) -> str:
        return self.title


class Portfolio(models.Model):
    """Портфолио"""
    title = models.CharField(
        max_length=100, default='')
    body = models.TextField()
    image = models.ImageField(
        upload_to='image')

    class Meta:
        verbose_name = 'Portfolio'
        db_table = 'portfolio'

    def __str__(self) -> str:
        return self.title