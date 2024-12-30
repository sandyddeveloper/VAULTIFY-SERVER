from django.db import models
from users.models import MyUser
class Transaction(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='transactions')
    transaction_id = models.CharField(max_length=100, unique=True, blank=False)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    transaction_type = models.CharField(max_length=20, choices=[('Credit', 'Credit'), ('Debit', 'Debit')])
    timestamp = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True)


class BankAccount(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='accounts')
    account_number = models.CharField(max_length=20, unique=True, blank=False)
    ifsc_code = models.CharField(max_length=11, blank=False)
    account_type = models.CharField(max_length=20, choices=[('Savings', 'Savings'), ('Current', 'Current')])
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0.0)
    created_at = models.DateTimeField(auto_now_add=True)

