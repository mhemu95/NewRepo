# Generated by Django 3.2.4 on 2021-09-07 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20210903_2151'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_img',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
