from django.contrib import admin
from .models import PedidoDesculpa

@admin.register(PedidoDesculpa)
class DesculpaAdmin(admin.ModelAdmin):
    list_display = ('text', 'color')
# Register your models here.
