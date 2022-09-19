from django.db import models

class WatchlistItem(models.Model):
    watched = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    rating = models.IntegerField(default=0)
    release_date = models.DateField(default = "0000-00-00")
    review = models.TextField(default = '')
