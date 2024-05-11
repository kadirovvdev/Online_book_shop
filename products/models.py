from django.db import models
# from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from users.models import CustomUser

# Create your models here.

class BookCategory(models.Model):
    name = models.CharField(max_length=100)


    class Meta:
        db_table = 'category_books'

    def __str__(self):
        return self.name

class Language(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'language'

    def __str__(self):
        return self.name

class Books(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    category = models.ForeignKey(BookCategory, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='books/', default='media/shadow.png')
    page = models.IntegerField()
    book_lang = models.ForeignKey(Language, on_delete=models.SET_DEFAULT, default='null')


    class Meta:
        db_table = 'books'

    def __str__(self):
        return self.title

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)


    class Meta:
        db_table = 'author'

class Book_author(models.Model):
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    class Meta:
        db_table = 'book_author'

    def __str__(self):
        return f"{self.author.first_name} + ' ' + {self.author.last_name}"


class Review(models.Model):
    comment = models.TextField()
    star_given = models.IntegerField(
        default=0,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0)
        ]
    )

    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)


    class Meta:
        db_table = 'review'

    def __str__(self):
        return self.comment