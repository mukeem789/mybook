from django.db import models
from book.models import Books
from account.models import Account

# Create your models here.
class UserActivity(models.Model):
    
    user_id                 = models.ForeignKey(Account, on_delete=models.CASCADE, default=1)
    book_id                 = models.ForeignKey(Books, on_delete=models.CASCADE, default=1)
    logged_in_time          = models.TimeField(auto_now=True)
    date                    = models.DateField(auto_now=True)
    unlocked_chapter        = models.BooleanField

    def __str__(self):
        return self.book_id