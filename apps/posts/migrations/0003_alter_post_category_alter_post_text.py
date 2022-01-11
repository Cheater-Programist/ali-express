# Generated by Django 4.0 on 2021-12-25 08:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0003_category_parent'),
        ('posts', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='продукт', to='categories.category'),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(blank=True, null=True, verbose_name='название'),
        ),
    ]
