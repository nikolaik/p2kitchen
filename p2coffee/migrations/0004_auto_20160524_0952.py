# Generated by Django 1.9.6 on 2016-05-24 09:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("p2coffee", "0003_auto_20160523_1253"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="coffeepotevent",
            options={
                "verbose_name": "Coffee pot event",
                "verbose_name_plural": "Coffee pot events",
            },
        ),
        migrations.AlterModelOptions(
            name="sensorevent",
            options={
                "verbose_name": "Sensor event",
                "verbose_name_plural": "Sensor events",
            },
        ),
        migrations.AlterIndexTogether(
            name="coffeepotevent",
            index_together=set([("created", "modified")]),
        ),
        migrations.AlterIndexTogether(
            name="sensorevent",
            index_together=set([("created", "modified")]),
        ),
    ]
