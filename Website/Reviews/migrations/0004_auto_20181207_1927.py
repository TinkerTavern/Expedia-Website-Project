# Generated by Django 2.1.4 on 2018-12-07 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reviews', '0003_auto_20181207_1527'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='datePosted',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='review',
            name='upvotes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='review',
            name='author',
            field=models.CharField(max_length=50, verbose_name='Author'),
        ),
        migrations.AlterField(
            model_name='review',
            name='location',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='review',
            name='reviewText',
            field=models.TextField(),
        ),
    ]
