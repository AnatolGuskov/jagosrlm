# Generated by Django 5.0.3 on 2024-04-30 08:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jagobasa', '0029_alter_collezione_options_alter_prodotto_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='prodotto',
            options={'ordering': ['nome']},
        ),
        migrations.RenameField(
            model_name='prodotto',
            old_name='nome_jago',
            new_name='nome',
        ),
        migrations.RemoveField(
            model_name='prodotto',
            name='nome_new',
        ),
    ]
