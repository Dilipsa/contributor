# Generated by Django 3.0.6 on 2020-05-09 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contributors', '0016_auto_20200509_1321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createcontributor',
            name='about',
            field=models.CharField(default='working as software developer', max_length=255),
        ),
    ]
