# Generated by Django 4.2.3 on 2023-08-07 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0004_portfolio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Имя навыка')),
                ('description', models.TextField(verbose_name='Описание навыка')),
            ],
            options={
                'verbose_name': 'Навык',
                'verbose_name_plural': 'Навыки',
            },
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': 'Коммент', 'verbose_name_plural': 'Комменты'},
        ),
        migrations.AlterModelOptions(
            name='portfolio',
            options={'verbose_name': 'Проекты', 'verbose_name_plural': 'Проекты'},
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='title',
            field=models.CharField(max_length=262, verbose_name='Заголовок проекта'),
        ),
    ]
