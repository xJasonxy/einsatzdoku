# Generated by Django 2.2.6 on 2019-11-16 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doku', '0010_einsatz_einsatzleiter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='einsatz',
            name='Einsatzleiter',
            field=models.CharField(default='', max_length=200),
        ),
    ]
