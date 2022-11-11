from django.contrib.auth.models import User
from django.db import models


class Women(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_created=True)
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE, related_name='my_books')
    author_1 = models.ManyToManyField(User, through='Like', related_name='books')

    def __str__(self):
        return f'{self.title}'


class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)

    def __str__(self):
        return f"{self.name}"


class Comment(models.Model):
    title = models.ForeignKey('Women', verbose_name='Заголовок', on_delete=models.CASCADE)
    author = models.ForeignKey(User, verbose_name='автор', on_delete=models.CASCADE)
    user = models.ForeignKey('Category', verbose_name='Категория', on_delete=models.CASCADE)
    time_now = models.DateTimeField(auto_now_add=True)
    content = models.TextField(blank=True)

    def __str__(self):
        return f"{self.author}"


class Like(models.Model):
    RATE_CHOICES = (
        (1, 'Ok'),
        (2, 'Good'),
        (3, 'Fine'),
        (4, 'Amazing'),
        (5, 'Incredible'),
    )
    user = models.ForeignKey(User, verbose_name='автор', on_delete=models.CASCADE)
    book = models.ForeignKey('Women',  on_delete=models.CASCADE)
    like = models.BooleanField(default=False)
    in_bookmarks = models.BooleanField(default=False)
    rate = models.PositiveIntegerField(choices=RATE_CHOICES, null=True)

    def __str__(self):
        return f'{self.book}'







