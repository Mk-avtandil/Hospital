# Generated by Django 4.0.4 on 2022-05-19 11:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0002_nurse_patient_treatdoctor_patient'),
    ]

    operations = [
        migrations.AddField(
            model_name='treatdoctor',
            name='hospital',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='mysite.hospital'),
            preserve_default=False,
        ),
    ]