from django.conf import settings
from django.db import models
from django.contrib.auth import get_user_model

class Article(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # 좋아요 기능에 필요한 author 필드 만들어야 함.
    
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    likes = models.ManyToManyField(get_user_model(), related_name='liked_comments', blank=True)
    
    def toggle_like(self, user):
        if user in self.likes.all():
            self.likes.remove(user)
        else:
            self.likes.add(user)