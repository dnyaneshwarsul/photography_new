from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'mobile', 'event_type', 'event_date', 'advance_amount', 'payment_status', 'booking_status', 'created_at')
    list_filter = ('event_type', 'payment_status', 'booking_status', 'created_at')
    search_fields = ('full_name', 'mobile', 'email', 'city', 'event_location', 'transaction_id')
