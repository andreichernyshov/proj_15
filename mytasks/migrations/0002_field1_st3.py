# Generated by Django 3.1.5 on 2021-01-29 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mytasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='field1',
            name='st3',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
