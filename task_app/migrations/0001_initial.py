# Generated by Django 3.2.5 on 2022-01-05 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('Id', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
    ]
