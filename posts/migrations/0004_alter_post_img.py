# Generated by Django 5.1.1 on 2025-02-24 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_post_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='posts/media/uploads/'),
        ),
    ]
