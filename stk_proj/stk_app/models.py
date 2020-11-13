from django.db import models

# Create your models here.
from martor.models import MartorField

class Post(models.Model):
    title = models.CharField(max_length=200)
    description = MartorField()
    wiki = MartorField(blank=True)
