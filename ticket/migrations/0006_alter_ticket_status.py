# Generated by Django 5.0 on 2024-01-03 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0005_alter_ticket_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='status',
            field=models.CharField(choices=[('Active', 'Active'), ('Resolved', 'Resolved'), ('Pending', 'Pending')], max_length=15),
        ),
    ]