# Generated by Django 4.2.3 on 2023-07-11 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=500)),
                ('email', models.EmailField(default='', max_length=2000)),
                ('message', models.TextField(default='', max_length=10000)),
            ],
        ),
    ]
