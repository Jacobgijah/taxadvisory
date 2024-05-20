from django.contrib import admin
from . import models

@admin.register(models.Message)
class MessageAdmin(admin.ModelAdmin):
  list_display = ['message', 'message_alert', 'created_at', 'message_status', 'customer']
  list_per_page = 10
  
  @admin.display(ordering='status')
  def message_status(self, message):
    if message.status == True:
      return 'Active'
    return 'Inactive'



@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
  list_display = ['first_name', 'last_name', 'phone', 'email', 'organization_type', 'organization_name', 'customer_status']
  ordering = ['first_name', 'last_name']
  list_per_page = 10

  @admin.display(ordering='status')
  def customer_status(self, customer):
    if customer.status == True:
      return 'Active'
    return 'Inactive'

admin.site.register(models.TaxRegion)
