# Generated by Django 4.2.1 on 2023-06-11 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
                ('phone', models.IntegerField(null=True)),
                ('joined_date', models.DateField(null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
    ]
