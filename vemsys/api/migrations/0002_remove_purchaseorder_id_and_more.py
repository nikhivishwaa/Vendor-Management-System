# Generated by Django 5.0 on 2023-12-31 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchaseorder',
            name='id',
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='po_number',
            field=models.CharField(editable=False, max_length=15, primary_key=True, serialize=False),
        ),
    ]