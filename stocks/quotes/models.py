from django.db import models

# Create your models here.

class Stock(models.Model):
    ticker_sym = models.CharField(max_length=10)

    def __str__(self):
        return self.ticker_sym