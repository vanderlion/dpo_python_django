# Generated by Django 4.1.7 on 2023-04-02 18:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0008_merge_20230328_0647'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['name', 'price']},
        ),
    ]
