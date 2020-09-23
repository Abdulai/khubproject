from django.db import models

class News(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    seats_available = models.IntegerField(blank=True)
    date = models.DateField()