from django.contrib import admin
from .models import User, Address, UserDetails

# Register your models here.
# class AddressInline(admin.TabularInline):
#     model = Address

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'password')
    readonly_fields = ('created',)
    fields = ('username', 'email', 'password', 'created')
    search_fields = ('username', 'email')
    list_filter = ('created',)

class UserDetailsAdmin(admin.ModelAdmin):
    list_display = ('first_name','second_name','last_name','second_last_name','doc_type', 'doc_number', 'telephone_number', 'user', 'address')    # campos que muestra
    fields = [('first_name','second_name'),('last_name','second_last_name'),('doc_type', 'doc_number'), 'telephone_number', 'user', 'address']    # orden
    search_fields = ('last_name','first_name','doc_number','telephone_number', 'address')                               # busqueda por escritura
    list_filter = ('last_name','doc_type','first_name', 'user')                                     # busqueda por filtro
    # inlines = [
    #     AddressInline,
    # ]

admin.site.register(User, UserAdmin)
admin.site.register(Address,)
admin.site.register(UserDetails, UserDetailsAdmin)