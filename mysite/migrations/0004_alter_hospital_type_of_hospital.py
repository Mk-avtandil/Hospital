# Generated by Django 4.0.4 on 2022-05-19 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0003_treatdoctor_hospital'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospital',
            name='type_of_hospital',
            field=models.CharField(choices=[(1, 'Государственная'), (0, 'Частная')], max_length=255),
        ),
    ]
