# Generated by Django 5.0.1 on 2024-02-01 17:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("students", "0002_alter_student_score"),
    ]

    operations = [
        migrations.AddField(
            model_name="student",
            name="email",
            field=models.EmailField(max_length=50, null=True),
        ),
    ]
