from django.db import models

class Books(models.Model):
    title = models.CharField(max_length=280, blank=False, null=False)
    # autor = models.CharField(max_length=280, blank=True, null=True)
    short_description = models.CharField(max_length=500, blank=True, null=True)
    cover = models.FileField(upload_to='covers/%Y/%m/%d/')
    pages = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.title