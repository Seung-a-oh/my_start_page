# Generated by Django 4.0.1 on 2022-01-31 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.CharField(max_length=10)),
                ('title', models.TextField()),
                ('link', models.TextField()),
            ],
        ),
    ]