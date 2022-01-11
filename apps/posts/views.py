from django.db.models import query
from rest_framework import viewsets
from apps.posts.models import Post,PostImage
from apps.posts import serializers

class PostAPIView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer

    def get_serializer_class(self):
        if self.action in ['retrieve']:
            return serializers.PostDetailSerializer
        return self.serializer_class
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        return 

class PostImageAPIView(viewsets.ModelViewSet):
    queryset = PostImage.objects.all()
    serializer_class = serializers.PostImageSerializer

