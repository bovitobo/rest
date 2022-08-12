from django.db import models


class Article(models.Model):
    name = models.CharField(max_length=200, default='')
    description = models.TextField(blank=True, default='')
    url = models.URLField(max_length=2000)
    rank = models.IntegerField(default=0)

    def __str__(self):
        return '%s' % self.name
