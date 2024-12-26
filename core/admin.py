from django.contrib import admin
from .models import Customer

# Register your models here.
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'total_amount', 'number_of_accounts')
    list_filter = ('total_amount', 'number_of_accounts')
    search_fields = ('first_name',)
    ordering = ('id',)
