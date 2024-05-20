from django.contrib import admin
from . import models

@admin.register(models.Message)
class MessageAdmin(admin.ModelAdmin):
  list_display = ['message', 'message_alert', 'created_at', 'status']
  list_editable = ['status']
  list_per_page = 10



@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
  list_display = ['first_name', 'last_name', 'phone', 'email', 'organization_type', 'organization_name']
  ordering = ['first_name', 'last_name']
  list_per_page = 10

admin.site.register(models.TaxRegion)
