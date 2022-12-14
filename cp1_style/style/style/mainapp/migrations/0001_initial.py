# Generated by Django 4.1 on 2022-09-07 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='information_user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(max_length=200)),
                ('age', models.IntegerField()),
                ('height', models.FloatField()),
                ('weight', models.FloatField()),
                ('large_category', models.CharField(max_length=200)),
                ('medium_category', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='review_user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(max_length=200)),
                ('recommend', models.CharField(max_length=200)),
                ('what', models.CharField(max_length=200)),
            ],
        ),
    ]
