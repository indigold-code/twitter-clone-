# Generated by Django 4.1.4 on 2023-05-11 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cloner', '0004_chirp_delete_clink'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
