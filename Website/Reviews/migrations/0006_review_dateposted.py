# Generated by Django 2.1.4 on 2018-12-07 21:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Reviews', '0005_remove_review_dateposted'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='datePosted',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
