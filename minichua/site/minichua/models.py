from django.db import models

class Mini(models.Model):
    name = models.CharField(max_length=200)
    image_url = models.CharField(max_length=200)
    tags = models.ManyToManyField('Tags', blank=True)

    def __str__(self):
        return self.name

class Tags(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name