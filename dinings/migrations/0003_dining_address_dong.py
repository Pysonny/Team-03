# Generated by Django 3.2.18 on 2023-05-07 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dinings', '0002_dining_address_gu'),
    ]

    operations = [
        migrations.AddField(
            model_name='dining',
            name='address_dong',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
