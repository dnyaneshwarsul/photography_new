from django.db import models

class Booking(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    )
    
    PAYMENT_STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Paid', 'Paid'),
        ('Failed', 'Failed'),
    )

    full_name = models.CharField(max_length=150)
    mobile = models.CharField(max_length=15)
    email = models.EmailField(max_length=150)
    city = models.CharField(max_length=100)
    password = models.CharField(max_length=128, null=True, blank=True)
    
    event_type = models.CharField(max_length=100)
    event_date = models.DateField()
    event_time = models.TimeField()
    event_location = models.CharField(max_length=255)
    guests = models.IntegerField(default=1, null=True, blank=True)
    duration = models.CharField(max_length=50, null=True, blank=True)
    
    service = models.CharField(max_length=100, null=True, blank=True)
    package = models.CharField(max_length=100, null=True, blank=True)
    budget = models.CharField(max_length=100, null=True, blank=True)
    reference_image = models.ImageField(upload_to="bookings/references/", null=True, blank=True)
    requirements = models.TextField(null=True, blank=True)
    
    payment_method = models.CharField(max_length=50, default="UPI")
    advance_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    remaining_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    remaining_payment_status = models.CharField(max_length=20, default='Pending')
    remaining_txn_id = models.CharField(max_length=100, null=True, blank=True)
    
    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUS_CHOICES, default='Pending')
    booking_status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    
    transaction_id = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_calculated_total_price(self):
        if self.total_price and self.total_price > 0:
            return float(self.total_price)
        import re
        if self.package:
            match = re.search(r'₹\s*([\d,]+)', self.package)
            if match:
                price_str = match.group(1).replace(',', '')
                return float(price_str)
        return 30000.00

    def get_remaining_due(self):
        if self.payment_status == 'Full Paid' or self.remaining_payment_status == 'Paid':
            return 0.0
        total = self.get_calculated_total_price()
        advance = float(self.advance_amount or 0)
        due = total - advance
        return max(0.0, due)

    def __str__(self):
        return f"Booking #{self.id} - {self.full_name} ({self.event_type})"


class ContactInquiry(models.Model):
    full_name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    phone = models.CharField(max_length=20)
    service = models.CharField(max_length=100, null=True, blank=True)
    event_date = models.DateField(null=True, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Inquiry from {self.full_name} ({self.service or 'General'})"

