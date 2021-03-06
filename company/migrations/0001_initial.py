# Generated by Django 2.0.6 on 2018-09-12 10:23

import company.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nazwa')),
                ('phone', models.CharField(blank=True, max_length=50, null=True, verbose_name='Telefon')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Utworzono')),
                ('email', models.CharField(default=' ', max_length=50, validators=[company.validators.validate_email], verbose_name='Email do firmy')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Zaktualizowano')),
                ('website', models.URLField(verbose_name='Strona Internetowa')),
                ('city', models.CharField(blank=True, max_length=64, verbose_name='Miasto')),
                ('street', models.CharField(blank=True, max_length=64, verbose_name='Ulica')),
                ('zip_code', models.CharField(blank=True, max_length=6, null=True, validators=[company.validators.validate_zip], verbose_name='Kod pocztowy')),
                ('industry', models.CharField(blank=True, max_length=64, verbose_name='Branża')),
                ('company_size', models.CharField(blank=True, max_length=64, verbose_name='Wielkość firmy')),
                ('krs_code', models.CharField(max_length=10, validators=[company.validators.validate_krs], verbose_name='Numer KRS')),
                ('nip_code', models.CharField(default=' ', max_length=10, validators=[company.validators.validate_nip], verbose_name='Numer NIP')),
                ('additional_info', models.TextField(blank=True, null=True, verbose_name='Dodatkowe Informacje')),
                ('privacy_email_date_send', models.DateTimeField(blank=True, null=True, verbose_name='Data powiadomienia o przetwarzaniu danych')),
            ],
            options={
                'verbose_name': 'Firma',
                'ordering': ['name'],
                'verbose_name_plural': 'Firmy',
            },
        ),
        migrations.CreateModel(
            name='CompanyContactPerson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255, verbose_name='Imię')),
                ('last_name', models.CharField(max_length=255, verbose_name='Nazwisko')),
                ('phone', models.CharField(blank=True, max_length=50, null=True, verbose_name='Telefon')),
                ('email', models.EmailField(default=' ', max_length=50, validators=[company.validators.validate_email], verbose_name='Email')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Utworzono')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Zaktualizowano')),
                ('privacy_email_date_send', models.DateTimeField(blank=True, null=True, verbose_name='Data powiadomienia o przetwarzaniu danych')),
            ],
            options={
                'verbose_name': 'Osoba do kontaktu Firmy współpracującej',
                'ordering': ['last_name', 'first_name'],
                'verbose_name_plural': 'Osoby do kontaktu Firmy współpracującej',
            },
        ),
        migrations.CreateModel(
            name='CompanyToCompanyContactPerson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Utworzono')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.Company', verbose_name='Firma')),
                ('company_contact_person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.CompanyContactPerson', verbose_name='Osoba do kontaktu Firmy współpracującej')),
            ],
            options={
                'verbose_name': 'Przypisana osoba',
                'ordering': ['-created_at'],
                'verbose_name_plural': 'Przypisane osoby',
            },
        ),
        migrations.CreateModel(
            name='EmailInformedUsers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='Email')),
                ('created_at', models.DateTimeField(verbose_name='Wysłano maila')),
            ],
            options={
                'verbose_name': 'Powiadomiona osoba',
                'ordering': ['email'],
                'verbose_name_plural': 'Powiadomione osoby',
            },
        ),
        migrations.AddField(
            model_name='company',
            name='company_contact_persons',
            field=models.ManyToManyField(related_name='companies', through='company.CompanyToCompanyContactPerson', to='company.CompanyContactPerson'),
        ),
    ]
