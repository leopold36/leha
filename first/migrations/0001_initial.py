# Generated by Django 2.0.5 on 2018-05-22 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enity_name', models.CharField(max_length=64)),
                ('entity_country', models.CharField(max_length=64)),
            ],
        ),
    ]
