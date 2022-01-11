from apps.users import  serializers
from apps.users.models import User
from rest_framework import viewsets

class UserAPIView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
