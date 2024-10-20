# Generated by Django 5.1.2 on 2024-10-17 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('denumire', models.CharField(max_length=100)),
                ('cantitate', models.CharField(max_length=50)),
                ('pret_studenti', models.DecimalField(decimal_places=2, max_digits=5)),
                ('imagine', models.ImageField(blank=True, null=True, upload_to='produse/')),
            ],
        ),
    ]
