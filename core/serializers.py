from .models import Customer
from rest_framework import serializers

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id','first_name', 'total_amount', 'number_of_accounts')