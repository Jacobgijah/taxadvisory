from django.contrib import admin
from django.db.models.aggregates import Count
from django.urls import reverse
from django.utils.html import format_html, urlencode
from . import models

@admin.register(models.Message)
class MessageAdmin(admin.ModelAdmin):
  autocomplete_fields = ['customer']
  actions = ['clear_inactive_messages']
  list_display = ['message', 'message_alert', 'message_status', 'customer']
  list_filter = ['message_alert', 'status', 'created_at']
  list_per_page = 10
  
  @admin.display(ordering='status')
  def message_status(self, message):
    if message.status == True:
      return 'Active'
    return 'Inactive'
  
  @admin.action(description='Clear Inactive Messages')
  def clear_inactive_messages(self, request, queryset):
    updated_query = queryset.update(status=0)
    self.message_user(
      request,
      f'{updated_query} messages were successfully updated.'
    )

  def get_queryset(self, request):
    return super().get_queryset(request).annotate(
      messages_count=Count('message')
    )
  

@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
  autocomplete_fields = ['user']
  list_display = ['first_name', 'last_name', 'phone', 'organization_type',
                  'organization_name', 'messages_count']
  
  list_per_page = 10
  list_select_related = ['user']
  ordering = ['user__first_name', 'user__last_name']
  search_fields = ['first_name__istartswith', 'last_name__istartswith']

  @admin.display(ordering='messages_count')
  def messages_count(self, customer):
    url = (
        reverse('admin:tax_message_changelist') 
        + '?'
        + urlencode({
          'customer__id': str(customer.id)
        }))
    return format_html('<a href="{}">{}</a>', url, customer.messages_count)    
  
  def get_queryset(self, request):
      return super().get_queryset(request).annotate(
        messages_count=Count('messages')
      )

@admin.register(models.TaxRegion)
class TaxRegion(admin.ModelAdmin):
  list_display = ['region', 'district']
  list_per_page = 10