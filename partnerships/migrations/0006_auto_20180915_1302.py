# Generated by Django 2.0.6 on 2018-09-15 11:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0003_auto_20180914_1248'),
        ('university', '0002_auto_20180913_2152'),
        ('partnerships', '0005_auto_20180914_1248'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contract',
            options={'get_latest_by': 'created_at', 'ordering': ['-contract_date'], 'verbose_name': 'Umowy', 'verbose_name_plural': 'Umowy'},
        ),
        migrations.AlterModelOptions(
            name='contracttocompanycontactperson',
            options={'ordering': ['-created_at'], 'verbose_name': 'Osoba do kontaktu Firmy współpracującej', 'verbose_name_plural': 'Osoby do kontaktu firmy współpracującej'},
        ),
        migrations.AlterModelOptions(
            name='contracttouniversitycontactperson',
            options={'ordering': ['-created_at'], 'verbose_name': 'Przypisana osoba UEK', 'verbose_name_plural': 'Przypisane osoby od strony UEK'},
        ),
        migrations.AddField(
            model_name='contract',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Utworzono'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='contracttocompanycontactperson',
            unique_together={('contract', 'company_contact_person')},
        ),
        migrations.AlterUniqueTogether(
            name='contracttouniversitycontactperson',
            unique_together={('contract', 'university_contact_person')},
        ),
    ]
