# Generated by Django 4.1.4 on 2023-01-14 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_subscriber_first_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(),
        ),
    ]