# Generated by Django 4.2.3 on 2023-08-03 05:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500, verbose_name='Заголовок статьи')),
                ('content', models.TextField(verbose_name='Текст статьи')),
                ('likes', models.IntegerField(verbose_name='Лайки')),
                ('image', models.ImageField(blank=True, null=True, upload_to='blogs_images', verbose_name='Главное изображение')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Статья',
                'verbose_name_plural': 'Статьи',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='User first name')),
                ('email', models.EmailField(max_length=254, verbose_name='User Email')),
                ('text', models.TextField(verbose_name='Comment Text')),
                ('data_created', models.DateTimeField(auto_now_add=True)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogs.blogs', verbose_name='Статья')),
                ('parent_comment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='child_comments', to='blogs.comment', verbose_name='Старший коммент')),
            ],
        ),
    ]
