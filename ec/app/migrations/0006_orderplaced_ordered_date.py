# Generated by Django 5.1.1 on 2024-10-02 13:15

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_product_category_payment_orderplaced'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderplaced',
            name='ordered_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
