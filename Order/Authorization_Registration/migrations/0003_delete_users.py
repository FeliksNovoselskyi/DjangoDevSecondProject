# Generated by Django 4.2.5 on 2023-11-06 18:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Authorization_Registration', '0002_alter_users_email_alter_users_login_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Users',
        ),
    ]
