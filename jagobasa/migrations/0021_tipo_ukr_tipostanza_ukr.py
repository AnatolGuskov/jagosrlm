# Generated by Django 5.0.3 on 2024-03-13 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jagobasa', '0020_tipostanza_alter_prodottoschede_scheda_blanc_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tipo',
            name='ukr',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='tipostanza',
            name='ukr',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
