# Generated by Django 2.2.3 on 2019-08-01 21:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Insta', '0002_auto_20190801_1908'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='post_on',
            new_name='posted_on',
        ),
    ]
