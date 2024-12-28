from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="First Name")
    last_name = models.CharField(max_length=50, verbose_name="Last Name")
    email = models.EmailField(unique=True, verbose_name="Email Address")
    account_name = models.CharField(max_length=50, verbose_name="Account Name")
    total_amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0.00,
        verbose_name="Total Amount"
    )
    number_of_accounts = models.PositiveIntegerField(
        default=0,
        verbose_name="Number of Accounts"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
