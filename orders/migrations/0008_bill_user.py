# Generated by Django 4.0.4 on 2022-05-09 15:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders', '0007_remove_bill_order_remove_bill_orderdetails_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
