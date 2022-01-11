from django.db.models import query
from rest_framework import viewsets
from apps.trash.models import Trash
from apps.trash import serializers

class TrashAPIView(viewsets.ModelViewSet):
    queryset = Trash.objects.all()
    serializer_class = serializers.TrashSerializer