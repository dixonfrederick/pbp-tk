# Generated by Django 3.2.8 on 2021-11-04 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diskusi', '0005_alter_discussion_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discussion',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]