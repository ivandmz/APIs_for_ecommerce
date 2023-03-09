from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=25, unique=True, verbose_name = 'Nombre de usuario')
    email = models.EmailField()
    password = models.CharField(max_length=32, verbose_name='Contraseña')
    created = models.DateTimeField(auto_now_add=True, verbose_name= 'Fecha registro')

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        ordering = ['username']

    def __str__(self):
        return self.username


class Address(models.Model):
    address_line1 = models.CharField(blank=True, null=True, max_length=100, verbose_name = 'Direccion. Primera línea')
    address_line2 = models.CharField(blank=True, null=True, max_length=100, verbose_name = 'Dirección. Segunda línea')
    city = models.CharField(blank=True, null=True, max_length=45, verbose_name = 'Ciudad')
    province = models.CharField(blank=True, null=True, max_length=45, verbose_name = 'Provincia')
    region = models.CharField(blank=True, null=True, max_length=45, verbose_name = 'Región')

    class Meta:
        verbose_name = 'Dirección'
        verbose_name_plural = 'Direcciones'
        ordering = ['region','province','city','address_line1']

    def __str__(self):
        return self.address_line1


class UserDetails(models.Model):
    TIPO_DOCUMENTO = (
        ('1', 'Cédula'),
        ('2', 'Pasaporte'),
    )
    first_name = models.CharField(max_length=45, verbose_name = 'Primer nombre')
    second_name = models.CharField(max_length=45,blank=True, null=True, verbose_name = 'Segundo nombre')
    last_name = models.CharField(max_length=45, verbose_name = 'Primer apellido')
    second_last_name = models.CharField(max_length=45,blank=True, null=True, verbose_name = 'Segundo apellido')
    doc_type = models.CharField(max_length=1, choices=TIPO_DOCUMENTO, verbose_name='Tipo Documento')
    doc_number = models.PositiveIntegerField(verbose_name='Numero documento')
    telephone_number =models.IntegerField(verbose_name='Teléfono')
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='UserDetails')
    address = models.ForeignKey(Address,default='', on_delete=models.CASCADE, related_name='UserDetails')

    class Meta:
        verbose_name = 'Detalles de usuario'
        verbose_name_plural = 'Detalles de usuarios'
        ordering = ['last_name','first_name']

    def __str__(self):
        return self.first_name +' '+ self.last_name + ' detalles'