# Generated by Django 4.1.4 on 2022-12-22 08:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_houses', '0004_alter_housetype_options_housetype_prestige_grade'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='housetype',
            options={'ordering': ['prestige_grade'], 'verbose_name': 'тип помещения', 'verbose_name_plural': 'типы помещений'},
        ),
    ]