# Generated by Django 3.2 on 2021-04-13 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('period', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='period',
            name='Period_date',
            field=models.DateTimeField(max_length=300),
        ),
    ]