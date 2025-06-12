from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Lead

@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'platform', 'inquiry_date', 'booking_status')
    list_filter = ('platform', 'booking_status')
    search_fields = ('name', 'phone')