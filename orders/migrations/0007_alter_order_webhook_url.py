# Generated by Django 4.1.3 on 2023-02-27 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_alter_order_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='webhook_url',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
