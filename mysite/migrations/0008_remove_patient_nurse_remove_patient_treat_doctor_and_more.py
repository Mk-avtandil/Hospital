# Generated by Django 4.0.4 on 2022-05-19 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0007_remove_nurse_patient_remove_treatdoctor_patient_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='nurse',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='treat_doctor',
        ),
        migrations.AddField(
            model_name='nurse',
            name='patient',
            field=models.ManyToManyField(to='mysite.patient'),
        ),
        migrations.AddField(
            model_name='treatdoctor',
            name='patient',
            field=models.ManyToManyField(to='mysite.patient'),
        ),
    ]
