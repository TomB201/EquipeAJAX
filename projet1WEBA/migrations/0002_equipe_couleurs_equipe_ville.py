# Generated by Django 4.1.3 on 2023-03-16 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projet1WEBA', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipe',
            name='couleurs',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='equipe',
            name='ville',
            field=models.CharField(max_length=64, null=True),
        ),
    ]
