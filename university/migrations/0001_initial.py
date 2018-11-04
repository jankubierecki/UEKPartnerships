# Generated by Django 2.0.6 on 2018-09-12 10:23

from django.db import migrations, models
import django.db.models.deletion
import university.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InstituteUnit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Nazwa')),
                ('additional_info', models.TextField(blank=True, null=True, verbose_name='Dodatkowe Informacje')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Utworzono')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Zaktualizowano')),
            ],
            options={
                'verbose_name': 'Jednostka Współpracująca UEK',
                'ordering': ['name'],
                'verbose_name_plural': 'Jednostki Współpracujące UEK',
            },
        ),
        migrations.CreateModel(
            name='InstituteUnitToUniversityContactPerson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Utworzono')),
                ('institute_unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='university.InstituteUnit', verbose_name='Jednostka Współpracująca UEK')),
            ],
            options={
                'verbose_name': 'Przypisana osoba',
                'ordering': ['-created_at'],
                'verbose_name_plural': 'Przypisane osoby',
            },
        ),
        migrations.CreateModel(
            name='UniversityContactPerson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255, verbose_name='Imię')),
                ('last_name', models.CharField(max_length=255, verbose_name='Nazwisko')),
                ('phone', models.CharField(blank=True, max_length=50, null=True, verbose_name='Telefon')),
                ('email', models.EmailField(help_text='Tylko z domeną UEK', max_length=50, validators=[university.validators.email_validation], verbose_name='Email')),
                ('academic_title', models.CharField(blank=True, max_length=50, null=True, verbose_name='Tytuł naukowy')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Utworzono')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Zaktualizowano')),
            ],
            options={
                'verbose_name': 'Osoba do kontaktu UEK',
                'ordering': ['last_name', 'first_name'],
                'verbose_name_plural': 'Osoby do kontaktu UEK',
            },
        ),
        migrations.AddField(
            model_name='instituteunittouniversitycontactperson',
            name='university_contact_person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='institute_units', to='university.UniversityContactPerson', verbose_name='Osoba do kontaktu UEK'),
        ),
        migrations.AddField(
            model_name='instituteunit',
            name='university_contact_persons',
            field=models.ManyToManyField(through='university.InstituteUnitToUniversityContactPerson', to='university.UniversityContactPerson'),
        ),
        migrations.AlterUniqueTogether(
            name='instituteunittouniversitycontactperson',
            unique_together={('institute_unit', 'university_contact_person')},
        ),
    ]
