# Generated by Django 4.0.3 on 2022-06-14 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_contactus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participate',
            name='value',
            field=models.CharField(choices=[('Participate', 'Participate'), ('Unparticipate', 'Unparticipate')], default='Participate', max_length=50),
        ),
    ]
