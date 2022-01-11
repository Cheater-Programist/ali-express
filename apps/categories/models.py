from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=255)
    parent =  models.ForeignKey('self',on_delete=models.CASCADE, related_name='under_category',blank=True,null=True)

    def __str__(self) -> str:
        return self.title