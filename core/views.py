from rest_framework.generics import RetrieveAPIView
from .models import Customer
from .serializers import DataSerializer

class UserInfoAPIView(RetrieveAPIView):
    serializer_class = DataSerializer
    queryset = Customer.objects.none()  

    def get_object(self):
        return Customer.objects.first()  
