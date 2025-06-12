from django import forms
from .models import Lead
from django.utils.translation import gettext_lazy as _

class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = '__all__'
        widgets = {
            'inquiry_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'notes': forms.Textarea(attrs={'rows': 3}),
        }
        labels = {
            'name': _('Name'),
            'phone': _('Phone Number'),
            'platform': _('Ad Platform'),
            'booking_status': _('Booking Status'),
            'reason': _('Reason for Not Booking'),
            'notes': _('Notes'),
        }