from django.db import models

from conduit.apps.core.models import TimestampedModel


class Article(TimestampedModel):
    slug = models.SlugField(db_index=True, max_length=255, unique=True)
    title = models.CharField(db_index=True, max_length=255)
    description = models.TextField()
    body = models.TextField()
    author = models.ForeignKey(
        'profiles.profile', on_delete=models.CASCADE, related_name='articles'
    )

    def __str__(self):
        return self.title


class Comment(TimestampedModel):
    body = models.TextField()
    article = models.ForeignKey(
        'articles.article', related_name='comments', on_delete=models.CASCADE
    )
    author = models.ForeignKey(
        'profiles.profile', related_name='comments', on_delete=models.CASCADE
    )
