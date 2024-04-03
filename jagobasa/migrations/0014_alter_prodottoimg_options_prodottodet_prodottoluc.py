# Generated by Django 5.0.2 on 2024-03-06 10:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jagobasa', '0013_collezione_image_back'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='prodottoimg',
            options={'ordering': ['img_nome']},
        ),
        migrations.CreateModel(
            name='ProdottoDet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('forma', models.CharField(max_length=5, null=True)),
                ('larghezza', models.IntegerField(blank=True, null=True)),
                ('profondita', models.IntegerField(blank=True, null=True)),
                ('altezza_min', models.IntegerField(blank=True, null=True)),
                ('altezza_max', models.IntegerField(blank=True, null=True)),
                ('catena', models.IntegerField(blank=True, null=True)),
                ('materiale', models.CharField(max_length=5, null=True)),
                ('variante', models.TextField(max_length=1000)),
                ('prodotto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='jagobasa.prodotto')),
            ],
            options={
                'ordering': ['prodotto'],
            },
        ),
        migrations.CreateModel(
            name='ProdottoLuc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lampadina', models.CharField(max_length=50, null=True)),
                ('quantita', models.IntegerField(blank=True, null=True)),
                ('prodotto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='jagobasa.prodotto')),
            ],
            options={
                'ordering': ['prodotto'],
            },
        ),
    ]
