from django.db import models

# Create your models here.
class Genre(models.Model):
    
    genre_name              = models.CharField(max_length=500)
    app_id                  = models.BigIntegerField

    def __str__(self):
        return self.genre_name
