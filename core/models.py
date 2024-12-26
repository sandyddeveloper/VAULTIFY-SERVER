from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=10)
    total_amount = models.DecimalField(max_digits=12, decimal_places=2)
    number_of_accounts = models.IntegerField()

    def __str__(self):
        return self.first_name
