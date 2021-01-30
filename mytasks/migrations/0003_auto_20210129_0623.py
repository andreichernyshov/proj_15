# Generated by Django 3.1.5 on 2021-01-29 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mytasks', '0002_field1_st3'),
    ]

    operations = [
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('st1', models.CharField(max_length=60)),
                ('st2', models.TextField()),
                ('st3', models.IntegerField(unique=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Field1',
        ),
    ]
