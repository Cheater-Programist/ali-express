from rest_framework import serializers
from apps.categories.models import Category
from apps.posts.models import Post,PostImage

class PostSerializer(serializers.ModelSerializer):
    user = serializers.CharField(read_only = True)

    class Meta:
        model = Post
        fields = '__all__'

class PostImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = PostImage
        fields = '__all__'

class PostDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

    