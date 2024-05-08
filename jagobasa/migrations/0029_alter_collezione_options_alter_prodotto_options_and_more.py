# Generated by Django 5.0.3 on 2024-04-30 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jagobasa', '0028_alter_collezione_nome_alter_tipo_eng_alter_tipo_ita_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='collezione',
            options={'ordering': ['nome']},
        ),
        migrations.AlterModelOptions(
            name='prodotto',
            options={'ordering': ['nome_jago']},
        ),
        migrations.AlterModelOptions(
            name='progetto',
            options={'ordering': ['nome']},
        ),
        migrations.RemoveField(
            model_name='prodotto',
            name='nome',
        ),
        migrations.AddField(
            model_name='prodotto',
            name='nome_jago',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='prodotto',
            name='nome_new',
            field=models.CharField(max_length=100, null=True),
        ),
    ]