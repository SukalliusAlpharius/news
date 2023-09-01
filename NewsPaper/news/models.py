from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class Author(models.Model):
    full_name = models.CharField(max_length=255)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


class Category(models.Model):
    Category_Name = models.CharField(max_length=255, unique=True)


class Post(models.Model):
    name = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    news_article = [
        (1, 'news'),
        (2, 'article')
    ]
    choice = models.PositiveSmallIntegerField(choices=news_article)
    text = models.TextField()
    rating = models.IntegerField(default=0)
    header = models.CharField(max_length=255)
    time_in = models.DateTimeField(auto_now_add=True)

    def like(self):
        Post.rating += 1
        return self

    def dislike(self):
        Post.rating -= 1
        return self

    def preview(self):

        return self[1:124] + "..."


class PostCategory(models.Model):
    post = models.ForeignKey("Post", on_delete=models.CASCADE)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey("Post", on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    time_in = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)

    def like(self):
        Comment.rating += 1
        return

    def dislike(self):
        Comment.rating -= 1
        return
