# Generated by Django 5.0.6 on 2024-05-17 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_remove_books_created_at_remove_books_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='created_at',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='books',
            name='updated_at',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
