# Generated by Django 2.2.5 on 2019-09-15 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='College_Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('College_name', models.CharField(max_length=100)),
                ('Address', models.TextField()),
                ('City', models.CharField(max_length=20)),
                ('State', models.CharField(max_length=20)),
                ('Contact_no', models.CharField(max_length=50)),
                ('Cut_off', models.PositiveIntegerField()),
            ],
        ),
    ]
