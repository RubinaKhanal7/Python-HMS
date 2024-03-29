# Generated by Django 4.1.3 on 2022-11-22 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('useraccounts', '0002_login_delete_register'),
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100, unique=True)),
                ('email', models.EmailField(max_length=254)),
                ('password1', models.CharField(max_length=100)),
                ('password2', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Register',
                'verbose_name_plural': 'Registers',
                'ordering': ('id',),
            },
        ),
    ]
