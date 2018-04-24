from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Article(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    about = models.CharField(max_length=200)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def likes(self):
        article_id = self.id
        return len(Favourite.objects.filter(article_id=article_id).filter(is_favourite=True))

    def __str__(self):
        return self.title


class Favourite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    is_favourite = models.BooleanField(default=False)
