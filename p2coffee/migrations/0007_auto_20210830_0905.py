# Generated by Django 3.2.6 on 2021-08-30 09:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("p2coffee", "0006_auto_20210826_1330"),
    ]

    operations = [
        migrations.AlterField(
            model_name="brew",
            name="machine",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name="brews", to="p2coffee.machine"
            ),
        ),
        migrations.AlterField(
            model_name="brewreaction",
            name="brew",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name="reactions", to="p2coffee.brew"
            ),
        ),
    ]
