# Generated by Django 5.1.3 on 2025-02-05 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='travel',
            name='comment',
            field=models.TextField(blank=True, null=True),
        ),
    ]
