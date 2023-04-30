from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=20)
    content = models.TextField()
    posted = models.DateTimeField('Date Posted')
    imageUrl = models.CharField(max_length=30, blank=True)


class Comments(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    commenter = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    content = models.TextField()
    posted = models.DateTimeField('Date Posted')
