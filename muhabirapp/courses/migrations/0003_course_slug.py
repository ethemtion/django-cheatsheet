# Generated by Django 4.2.3 on 2023-08-16 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]
