# Generated by Django 4.0.4 on 2022-05-19 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0011_remove_treatdoctor_patient_treatdoctor_patient'),
    ]

    operations = [
        migrations.AddField(
            model_name='maindoctor',
            name='image',
            field=models.FileField(default=1, upload_to='media/%Y/%m/%d'),
            preserve_default=False,
        ),
    ]
