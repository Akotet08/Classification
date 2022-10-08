# Generated by Django 4.1.2 on 2022-10-07 16:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0008_alter_image_upload_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="image",
            name="upload_date",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
    ]
