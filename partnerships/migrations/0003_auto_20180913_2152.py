# Generated by Django 2.0.6 on 2018-09-13 19:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('partnerships', '0002_auto_20180912_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='company_contact_persons',
            field=models.ForeignKey(help_text='Osoby do kontaktu firmy związane z tą umową', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='contracts', to='company.CompanyContactPerson', verbose_name='Osoby Do kontaktu Firmy'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='university_contact_persons',
            field=models.ForeignKey(help_text='Osoby do kontaktu UEK związane z tą umową', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='contracts', to='university.UniversityContactPerson', verbose_name='Osoby Do kontaktu UEK'),
        ),
    ]