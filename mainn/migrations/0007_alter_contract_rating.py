# Generated by Django 3.2 on 2021-05-07 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainn', '0006_alter_contract_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='rating',
            field=models.TextField(null=True),
        ),
    ]
