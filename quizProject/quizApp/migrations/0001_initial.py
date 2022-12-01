# Generated by Django 4.1.3 on 2022-12-01 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="QuizModel",
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
                ("question", models.CharField(max_length=250, null=True)),
                ("option1", models.CharField(max_length=250, null=True)),
                ("option2", models.CharField(max_length=250, null=True)),
                ("option3", models.CharField(max_length=250, null=True)),
                ("option4", models.CharField(max_length=250, null=True)),
                ("ans", models.CharField(max_length=250, null=True)),
            ],
        ),
    ]
