# Generated by Django 4.1.7 on 2023-03-01 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peak', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RejectedConnexion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(blank=True, max_length=2, null=True)),
                ('country_code', models.CharField(blank=True, max_length=15, null=True)),
            ],
            options={
                'verbose_name': 'RejectedConnexion',
                'verbose_name_plural': 'RejectedConnexions',
            },
        ),
    ]
