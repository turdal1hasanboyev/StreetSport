# Generated by Django 5.2 on 2025-04-05 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stadium', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stadium',
            name='image',
            field=models.ImageField(default='img/default.png', upload_to='stadiums/'),
        ),
    ]
