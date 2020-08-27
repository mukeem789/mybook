from django.db import models
from book.models import Books

# Create your models here.
class UserCollection(models.Model):
    
    book_id                 = models.ForeignKey(Books, on_delete=models.CASCADE, default=1)
    logged_in_time          = models.TimeField(auto_now=True)

    def __str__(self):
        return self.book_id