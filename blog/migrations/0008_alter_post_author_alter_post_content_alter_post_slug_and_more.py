# Generated by Django 4.0.1 on 2022-03-06 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_post_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.CharField(max_length=14),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.CharField(max_length=130),
        ),
        migrations.AlterField(
            model_name='post',
            name='timeStamp',
            field=models.DateTimeField(blank=True),
        ),
    ]
