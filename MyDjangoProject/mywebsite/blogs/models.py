from django.db import models


# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.first_name + " " + self.last_name

class Tag(models.Model):
    caption = models.CharField(max_length=50)
    def __str__(self):
        return self.caption


class Post(models.Model):
    title = models.CharField(max_length=200)
    preview = models.CharField(max_length=300)
    content = models.TextField()
    date = models.DateField(auto_now=True)
    slug = models.SlugField(max_length=50, unique=True)
    image = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    tag = models.ManyToManyField(Tag)
    def __str__(self):
        return self.title

class Comment(models.Model):
    user_name = models.CharField(max_length=50)
    user_email = models.EmailField()
    comments = models.TextField()
    date = models.DateField(auto_now=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")




