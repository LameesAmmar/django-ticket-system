# Generated by Django 5.0 on 2024-01-02 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0003_alter_ticket_engineer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='resolution_steps',
            field=models.TextField(blank=True, null=True),
        ),
    ]
