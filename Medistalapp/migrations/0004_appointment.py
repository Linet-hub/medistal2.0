# Generated by Django 5.0.6 on 2024-07-09 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Medistalapp', '0003_company'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=10)),
                ('date', models.DateField()),
                ('department', models.CharField(max_length=200)),
                ('doctor', models.CharField(max_length=200)),
                ('message', models.TextField()),
            ],
        ),
    ]
