# Generated by Django 4.2.6 on 2023-11-02 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_license_driver_licence'),
    ]

    operations = [
        migrations.CreateModel(
            name='slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=50)),
                ('text1', models.EmailField(max_length=254)),
                ('image', models.ImageField(default='uploads/slider/profile.jpg', upload_to='uploads/slider')),
            ],
        ),
    ]
