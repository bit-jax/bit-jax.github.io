from django.db import models

class Mini(models.Model):
    name = models.CharField()
    image_url = models.CharField()
    tags = models.ManyToOne()

    def __str__(self):
        return self.name

class Tags(models.Model):
    name = models.CharField()

    def __str__(self):
        return self.name