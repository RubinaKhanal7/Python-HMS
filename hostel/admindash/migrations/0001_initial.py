# Generated by Django 4.1.3 on 2022-11-21 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_id', models.IntegerField()),
                ('no_of_beds', models.IntegerField()),
                ('floor_number', models.IntegerField()),
                ('price', models.IntegerField()),
                ('status', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Room',
                'verbose_name_plural': 'Rooms',
                'ordering': ('room_id',),
            },
        ),
    ]
