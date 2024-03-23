from django.contrib import admin
from .models import Pago


# Register your models here.
@admin.register(Pago)
class PagoAdmin(admin.ModelAdmin):
    list_display = ('user', 'session', 'rising', 'date')
    search_fields = ('user_username', 'session_user_username')
