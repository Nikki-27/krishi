# Generated by Django 4.0 on 2021-12-12 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000000)),
                ('phone', models.CharField(max_length=10)),
                ('city', models.CharField(max_length=10000)),
                ('state', models.CharField(max_length=100000)),
                ('zip', models.CharField(max_length=10000)),
                ('ntractor', models.IntegerField()),
                ('implements', models.CharField(max_length=10000)),
            ],
        ),
    ]
