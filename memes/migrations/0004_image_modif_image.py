# Generated by Django 4.1.1 on 2025-03-19 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memes', '0003_delete_meme_image_text_alter_image_caption_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='modif_image',
            field=models.ImageField(blank=True, null=True, upload_to='modif_images/'),
        ),
    ]
