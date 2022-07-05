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
        return self.post
