# Generated by Django 4.1.5 on 2023-01-31 04:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('api_inventary', '0001_initial'),
        ('api_users', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('products_amount', models.PositiveIntegerField(null=True, verbose_name='Cantidad productos')),
                ('total_sale', models.FloatField(null=True, verbose_name='Total venta')),
                ('products', models.ManyToManyField(related_name='Tickets', to='api_inventary.product')),
            ],
            options={
                'verbose_name': 'Ticket',
                'verbose_name_plural': 'Tickets',
                'ordering': ['-pk'],
            },
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_sale', models.PositiveIntegerField(verbose_name='Número venta')),
                ('date_sale', models.DateTimeField(auto_now_add=True, verbose_name='Fecha venta')),
                ('installments_interval', models.PositiveIntegerField(null=True, verbose_name='Intervalo cuotas')),
                ('initial_deposit', models.FloatField(verbose_name='Abono inicial')),
                ('installments_amount', models.PositiveSmallIntegerField(verbose_name='Cantidad cuotas')),
                ('ticket', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Venta', to='api_sales.ticket')),
                ('user_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Ventas', to='api_users.userdetails')),
            ],
            options={
                'verbose_name': 'Venta',
                'verbose_name_plural': 'Ventas',
                'ordering': ['-date_sale'],
            },
        ),
        migrations.CreateModel(
            name='Charge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment', models.FloatField(verbose_name='Abono')),
                ('historical_balance', models.FloatField(null=True, verbose_name='Saldo histórico')),
                ('payment_date', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de abono')),
                ('sale', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Cobros', to='api_sales.sale')),
                ('user_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Cobros', to='api_users.userdetails')),
            ],
            options={
                'verbose_name': 'Cobro',
                'verbose_name_plural': 'Cobros',
                'ordering': ['-payment_date'],
            },
        ),
    ]
