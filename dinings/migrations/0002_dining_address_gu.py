# Generated by Django 3.2.18 on 2023-05-07 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dinings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dining',
            name='address_gu',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
