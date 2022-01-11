from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.fields import related
from apps.categories.models import Category

User = get_user_model()

class Post(models.Model):
    text = models.CharField(max_length=200,null=True, blank=True,verbose_name='название')
    created_at = models.DateField(auto_now=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='post_user')
    category = models.ForeignKey(Category,on_delete=models.CASCADE,blank=True,null=True,related_name='продукт')
    price = models.PositiveIntegerField(verbose_name='Цена')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')

    def __str__(self):
        return str(self.text)

class PostImage(models.Model):
    image = models.ImageField(upload_to = 'image',null=True, blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_image',null=True, blank=True)
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='post_image',null=True, blank=True)
