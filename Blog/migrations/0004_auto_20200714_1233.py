# Generated by Django 3.0.8 on 2020-07-14 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0003_blogcomment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='desc',
            field=models.TextField(),
        ),
    ]