# Generated by Django 4.1.2 on 2022-11-14 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_brand_facebook_followers_brand_instagram_followers_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Admin',
            new_name='Employee',
        ),
        migrations.RenameField(
            model_name='brand',
            old_name='come_name',
            new_name='company_name',
        ),
        migrations.AddField(
            model_name='user',
            name='is_employee',
            field=models.BooleanField(default=False),
        ),
    ]
