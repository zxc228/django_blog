# Generated by Django 5.1 on 2024-09-02 15:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='poast',
            new_name='post',
        ),
    ]
