# Generated by Django 2.0.5 on 2018-06-15 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0006_auto_20180614_1512'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='privacy_email_date_send',
            field=models.DateTimeField(auto_now=True, verbose_name='Data powiadomienia o przetwarzaniu danych osobowych'),
        ),
        migrations.AddField(
            model_name='companycontactperson',
            name='privacy_email_date_send',
            field=models.DateTimeField(auto_now=True, verbose_name='Data powiadomienia o przetwarzaniu danych osobowych'),
        ),
    ]