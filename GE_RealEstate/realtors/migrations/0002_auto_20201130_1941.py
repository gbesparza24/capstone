# Generated by Django 3.1.2 on 2020-12-01 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realtor',
            name='picture',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
