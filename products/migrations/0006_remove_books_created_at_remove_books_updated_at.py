# Generated by Django 5.0.6 on 2024-05-16 12:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_books_created_at_books_updated_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='books',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='books',
            name='updated_at',
        ),
    ]