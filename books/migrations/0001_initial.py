# Generated by Django 4.2.2 on 2023-06-08 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('sub_name', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('isbn', models.CharField(max_length=13)),
                ('price', models.DecimalField(decimal_places=2, max_digits=30)),
            ],
        ),
    ]
