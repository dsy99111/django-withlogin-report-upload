# Generated by Django 5.0.3 on 2024-03-26 17:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("patients", "0003_alter_testreport_patient"),
    ]

    operations = [
        migrations.AddField(
            model_name="patient",
            name="age",
            field=models.IntegerField(default=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="patient",
            name="name",
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
