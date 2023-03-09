from django.contrib import admin
from .models import Ticket, Sale, Charge

# Register your models here.
# class TicketAdmin(admin.ModelAdmin):

admin.site.register(Ticket)
admin.site.register(Sale)
admin.site.register(Charge)