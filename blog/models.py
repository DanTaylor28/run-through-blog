from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=250)
    title_tag = models.CharField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=100, default='General')

    def __str__(self):
        return f"{self.title} | {self.author}"

    def get_absolute_url(self):
        # return reverse('article_detail', args=str(self.id))
        return reverse('home')

