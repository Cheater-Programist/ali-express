from rest_framework import serializers
from apps.trash.models import Trash

class TrashSerializer(serializers.ModelSerializer):
    # user = serializers.CharField(read_only = True)

    class Meta:
        model = Trash
        fields = '__all__'