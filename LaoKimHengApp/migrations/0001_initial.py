# Generated by Django 2.0.4 on 2018-04-29 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserAccount',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=10)),
            ],
        ),
    ]