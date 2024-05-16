from django.contrib import admin
from tax.models import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
  list_display = ['first_name', 'last_name', 'phone', 'organization_type', 'status']

