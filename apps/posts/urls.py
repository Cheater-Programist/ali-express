from rest_framework import routers
from rest_framework.routers import DefaultRouter
from apps.posts.views import PostAPIView,PostImageAPIView
from apps.users.views import UserAPIView
from apps.categories.views import CategoryAPIView

router = DefaultRouter()
router.register('post',PostAPIView,basename='post_api')
router.register('post_image',PostImageAPIView,basename='post_image_api')
router.register('category',CategoryAPIView,basename='category_api')
router.register('user',UserAPIView,basename='user_api')
urlpatterns = router.urls