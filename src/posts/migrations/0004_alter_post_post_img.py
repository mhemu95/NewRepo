# Generated by Django 3.2.7 on 2021-09-07 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_post_post_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_img',
            field=models.ImageField(blank=True, default='default_image.jpg', null=True, upload_to=''),
        ),
    ]
