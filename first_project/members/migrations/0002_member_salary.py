# Generated by Django 4.1.4 on 2022-12-30 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='salary',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
