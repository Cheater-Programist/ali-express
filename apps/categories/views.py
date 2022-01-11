from rest_framework import viewsets
from apps.categories.models import Category
from apps.categories import serializers

class CategoryAPIView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer
