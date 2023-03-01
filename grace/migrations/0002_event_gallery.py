# Generated by Django 4.1 on 2023-02-19 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("grace", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Event_Gallery",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("image", models.ImageField(blank=True, upload_to="users/%Y/%m/%d/")),
                ("title", models.CharField(max_length=200, unique=True)),
                ("image2", models.ImageField(blank=True, upload_to="users/%Y/%m/%d/")),
                ("title2", models.CharField(max_length=200, unique=True)),
                ("image3", models.ImageField(blank=True, upload_to="users/%Y/%m/%d/")),
                ("title3", models.CharField(max_length=200, unique=True)),
                ("image4", models.ImageField(blank=True, upload_to="users/%Y/%m/%d/")),
                ("title4", models.CharField(max_length=200, unique=True)),
                ("image5", models.ImageField(blank=True, upload_to="users/%Y/%m/%d/")),
                ("title5", models.CharField(max_length=200, unique=True)),
                ("image6", models.ImageField(blank=True, upload_to="users/%Y/%m/%d/")),
                ("title6", models.CharField(max_length=200, unique=True)),
                ("date", models.DateTimeField(auto_now=True)),
            ],
        ),
    ]