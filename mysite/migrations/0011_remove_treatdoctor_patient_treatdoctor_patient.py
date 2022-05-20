# Generated by Django 4.0.4 on 2022-05-19 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0010_remove_treatdoctor_patient_treatdoctor_patient'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='treatdoctor',
            name='patient',
        ),
        migrations.AddField(
            model_name='treatdoctor',
            name='patient',
            field=models.ManyToManyField(to='mysite.patient'),
        ),
    ]