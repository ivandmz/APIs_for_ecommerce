from django.db import models
from api_inventary.models import Product
from api_users.models import UserDetails

# Create your models here.
class Ticket(models.Model):
    products_amount = models.PositiveIntegerField(null=True, verbose_name='Cantidad productos')
    total_sale = models.FloatField(null=True, verbose_name='Total venta')
    products = models.ManyToManyField(Product, related_name='Tickets')

    class Meta:
        verbose_name = 'Ticket'
        verbose_name_plural = 'Tickets'
        ordering = ['-pk']

    def __str__(self):
        return f'{self.total_sale}'


class Sale(models.Model):
    """The amont of every transaction"""
    num_sale = models.PositiveIntegerField(verbose_name='Número venta')
    date_sale = models.DateTimeField(auto_now_add=True, verbose_name= 'Fecha venta')
    installments_interval = models.PositiveIntegerField(null=True, verbose_name='Intervalo cuotas') # será la cant de dias entre cada pago..?
    initial_deposit = models.FloatField(verbose_name='Abono inicial')
    installments_amount = models.PositiveSmallIntegerField(verbose_name='Cantidad cuotas')
    ticket = models.OneToOneField(Ticket, on_delete=models.CASCADE, related_name='Venta')
    user_details = models.ForeignKey(UserDetails, on_delete=models.CASCADE, related_name='Ventas')

    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'
        ordering = ['-date_sale']

    def __str__(self):
        return f'{self.num_sale}'


class Charge(models.Model):
    payment = models.FloatField(verbose_name='Abono')
    historical_balance = models.FloatField(null=True, verbose_name='Saldo histórico')
    payment_date = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de abono')
    user_details = models.ForeignKey(UserDetails, on_delete=models.CASCADE, related_name='Cobros')
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE, related_name='Cobros')

    class Meta:
        verbose_name = 'Cobro'
        verbose_name_plural = 'Cobros'
        ordering = ['-payment_date']

    def __str__(self):
        return f'{self.payment}'