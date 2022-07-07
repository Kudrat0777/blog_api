from django.contrib import admin
from .models import Portfolio, Post, Comment, Category, Service


admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Portfolio)
admin.site.register(Service)


