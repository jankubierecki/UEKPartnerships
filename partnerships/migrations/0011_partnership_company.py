# Generated by Django 2.0.6 on 2018-10-03 17:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0004_auto_20181002_1729'),
        ('partnerships', '0010_auto_20181003_1924'),
    ]

    operations = [
        migrations.AddField(
            model_name='partnership',
            name='company',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='partnerships', to='company.Company', verbose_name='Firma'),
            preserve_default=False,
        ),
    ]