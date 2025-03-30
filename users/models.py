from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', null=True, blank=True)
    liked_blogs = models.ManyToManyField('blogs.Blogs')


class Testimonials(models.Model):
    full_name = models.CharField(max_length=255, verbose_name='Полное имя клиента')
    designation = models.CharField(max_length=255, verbose_name='Обозначение клиента')
    opinion = models.TextField(verbose_name='Мнение клиента')

    image = models.ImageField(upload_to='testimonials_images', null=True, blank=True)
    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

    def __str__(self):
        return self.full_name


