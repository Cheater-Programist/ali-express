from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.fields import related
from apps.posts.models import Post

User = get_user_model()

class Trash(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='trash_post',null=True, blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='trash_user',null=True, blank=True)
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')

    def __str__(self) -> str:
        return self.post