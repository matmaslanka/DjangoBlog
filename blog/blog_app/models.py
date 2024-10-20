from django.db import models

from django.contrib.auth.models import User

# Create your models here.


class Entries(models.Model):
    title = models.CharField(max_length=100, blank=False)
    slug = models.SlugField(unique=True)
    content = models.TextField(max_length=1000, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

