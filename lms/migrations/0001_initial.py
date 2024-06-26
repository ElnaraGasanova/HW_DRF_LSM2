# Generated by Django 5.0.4 on 2024-04-11 18:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Укажите наименование курса', max_length=150, verbose_name='Наименование')),
                ('image', models.ImageField(blank=True, help_text='Загрузите превью курса', null=True, upload_to='courses_image', verbose_name='Превью')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Курс',
                'verbose_name_plural': 'Курсы',
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Укажите наименование урока', max_length=100, verbose_name='Наименование')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('image', models.ImageField(blank=True, help_text='Загрузите превью урока', null=True, upload_to='lessons_image', verbose_name='Превью')),
                ('video_link', models.URLField(blank=True, help_text='Укажите ссылку на видео', null=True, verbose_name='Ссылка')),
                ('course', models.ForeignKey(help_text='Укажите наименование курса', on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='lms.course', verbose_name='Курс')),
            ],
            options={
                'verbose_name': 'Урок',
                'verbose_name_plural': 'Уроки',
            },
        ),
    ]
