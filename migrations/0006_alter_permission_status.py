# Generated by Django 3.2.8 on 2021-11-26 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('no_dues', '0005_authority_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permission',
            name='status',
            field=models.CharField(choices=[('nrq', 'Not Requested'), ('req', 'Requested'), ('rep', 'Reported'), ('nap', 'Not Applicable'), ('apc', 'Approved On Condition'), ('app', 'Approved')], default='nrq', max_length=3),
        ),
    ]
