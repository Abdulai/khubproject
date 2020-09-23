from django.db import models

class Page(models.Model):
    name = models.CharField(max_length=100)
    area_of_study = models.CharField(max_length=200)
    project_completed = models.CharField(max_length=400)
    ongoing_project = models.CharField(max_length=500)

    def __str__(self):
        return self.name