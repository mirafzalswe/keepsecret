from django.contrib import admin
from .models import Post,Comment, Like,Hashtag
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Hashtag)
admin.site.register(Like)
# Register your models here.
