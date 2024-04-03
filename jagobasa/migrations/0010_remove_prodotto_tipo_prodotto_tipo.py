# Generated by Django 5.0.2 on 2024-03-03 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jagobasa', '0009_tipo_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prodotto',
            name='tipo',
        ),
        migrations.AddField(
            model_name='prodotto',
            name='tipo',
            field=models.ManyToManyField(help_text='Select a tipo for this poem', to='jagobasa.tipo'),
        ),
    ]
