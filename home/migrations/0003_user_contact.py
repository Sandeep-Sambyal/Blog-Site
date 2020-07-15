# Generated by Django 3.0.8 on 2020-07-11 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0002_delete_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_contact',
            fields=[
                ('name', models.CharField(max_length=70)),
                ('email', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=15)),
                ('sno', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
    ]