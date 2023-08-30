from django.db import models
from django.utils import timezone


class Blogs(models.Model):
    author = models.ForeignKey('users.User', verbose_name="Автор", on_delete=models.CASCADE)
    title = models.CharField(verbose_name="Заголовок статьи", max_length=500)
    slug = models.SlugField(max_length=255, unique=True, verbose_name="Ссылка на статью")
    content = models.TextField(verbose_name="Текст статьи")
    # likes = models.IntegerField(verbose_name="Лайки", default=0)
    image = models.ImageField(upload_to="blogs_images", verbose_name="Главное изображение",)
    date_created = models.DateTimeField(auto_now_add=True)
    publish = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"

    def __str__(self):
        return self.title


class Comment(models.Model):
    parent_comment = models.ForeignKey('Comment', related_name="child_comments", verbose_name="Старший коммент",
                                       on_delete=models.CASCADE, blank=True, null=True)
    blog = models.ForeignKey(Blogs, verbose_name="Статья", on_delete=models.CASCADE)
    name = models.CharField(max_length=255, verbose_name="User first name")
    email = models.EmailField(verbose_name="User Email")
    text = models.TextField(verbose_name="Comment Text")
    data_created = models.DateTimeField(auto_now_add=True)

    @property
    def get_childs(self):
        return self.child_comments.all()

    class Meta:
        verbose_name = "Коммент"
        verbose_name_plural = "Комменты"

    def __str__(self):
        return f'{self.email} {self.text}'


class Portfolio(models.Model):
    name = models.CharField(verbose_name="Имя проекта", max_length=255)
    title = models.CharField(verbose_name="Заголовок проекта", max_length=262)
    description = models.TextField(verbose_name="Описание проекта")
    link = models.URLField(verbose_name="Сссылка на проект")
    image = models.ImageField(verbose_name="Изображение проекта", upload_to="portfolio_images")

    class Meta:
        verbose_name = "Проекты"
        verbose_name_plural = "Проекты"

    def __str__(self):
        return self.name


class Skills(models.Model):
    title = models.CharField(verbose_name="Имя навыка", max_length=255)
    description = models.TextField(verbose_name="Описание навыка")

    class Meta:
        verbose_name = "Навык"
        verbose_name_plural = "Навыки"

    def __str__(self):
        return self.title


class Services(models.Model):
    name = models.CharField(verbose_name="Имя услуги", max_length=255)
    description = models.TextField(verbose_name="Подробности услуги")
    image = models.ImageField(upload_to="service_images")

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"

    def __str__(self):
        return self.name


class Messages(models.Model):
    name = models.CharField(verbose_name="Имя отправителя", max_length=255)
    email = models.EmailField(verbose_name="Электронной адресс отправителя")
    message = models.TextField(verbose_name="Сообщение")

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"

    def __str__(self):
        return self.name
