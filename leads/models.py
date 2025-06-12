from django.db import models

# Create your models here.
from django.db import models
from django.utils.translation import gettext_lazy as _

class Lead(models.Model):
    PLATFORM_CHOICES = [
        ('instagram', _('Instagram')),
        ('whatsapp', _('WhatsApp')),
        ('facebook', _('Facebook')),
        ('other', _('Other')),
    ]
    
    BOOKING_STATUS = [
        ('booked', _('Booked Appointment')),
        ('not_booked', _('Did Not Book')),
        ('follow_up', _('Needs Follow Up')),
    ]
    
    REASON_CHOICES = [
        ('price', _('Price Concerns')),
        ('location', _('Location Not Convenient')),
        ('timing', _('Timing Not Suitable')),
        ('other_doctor', _('Preferred Another Doctor')),
        ('other', _('Other Reason')),
    ]
    
    name = models.CharField(_('Name'), max_length=100)
    phone = models.CharField(_('Phone Number'), max_length=20)
    platform = models.CharField(_('Ad Platform'), max_length=20, choices=PLATFORM_CHOICES)
    inquiry_date = models.DateTimeField(_('Inquiry Date'), auto_now_add=True)
    booking_status = models.CharField(_('Booking Status'), max_length=20, choices=BOOKING_STATUS)
    reason = models.CharField(_('Reason for Not Booking'), max_length=20, choices=REASON_CHOICES, blank=True, null=True)
    notes = models.TextField(_('Notes'), blank=True)
    
    class Meta:
        verbose_name = _('Lead')
        verbose_name_plural = _('Leads')
    
    def __str__(self):
        return f"{self.name} - {self.get_platform_display()}"