# Generated by Django 5.0 on 2023-12-29 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='vendor_code',
            field=models.CharField(editable=False, max_length=10, primary_key=True, serialize=False),
        ),
    ]
