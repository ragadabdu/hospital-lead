from django.views.generic import ListView, CreateView, UpdateView, TemplateView
from django.urls import reverse_lazy
from .models import Lead
from .forms import LeadForm
from django.contrib.auth.mixins import LoginRequiredMixin

class LeadUpdateView(LoginRequiredMixin, UpdateView):
    success_message = "تم تحديث بيانات العميل بنجاح"
    model = Lead
    form_class = LeadForm
    template_name = 'leads/lead_form.html'
    success_url = reverse_lazy('leads:lead_list')

class LeadListView(LoginRequiredMixin, ListView):
    model = Lead
    template_name = 'leads/lead_list.html'
    context_object_name = 'leads'
    ordering = ['-inquiry_date']  # Newest first
    paginate_by = 20  # Show 20 leads per page

class LeadCreateView(LoginRequiredMixin, CreateView):
    login_url = '/accounts/login/'
    redirect_field_name = 'next'
    model = Lead
    form_class = LeadForm
    template_name = 'leads/lead_form.html'
    success_url = reverse_lazy('leads:dashboard')

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'leads/dashboard.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Get choice display values properly
        platform_choices = dict(Lead.PLATFORM_CHOICES)
        booking_status_choices = dict(Lead.BOOKING_STATUS)
        reason_choices = dict(Lead.REASON_CHOICES)
        
        # Platform analytics
        platform_data = []
        for platform_value, platform_name in Lead.PLATFORM_CHOICES:
            total = Lead.objects.filter(platform=platform_value).count()
            booked = Lead.objects.filter(platform=platform_value, booking_status='booked').count()
            platform_data.append({
                'name': platform_name,  # Use the display name directly
                'value': platform_value,
                'total': total,
                'booked': booked,
                'conversion_rate': round((booked/total)*100, 2) if total > 0 else 0
            })
        
        context['platform_data'] = platform_data
        context['total_leads'] = Lead.objects.count()
        context['total_booked'] = Lead.objects.filter(booking_status='booked').count()
        
        # Reasons for not booking
        reason_data = []
        for reason_value, reason_name in Lead.REASON_CHOICES:
            count = Lead.objects.filter(reason=reason_value).count()
            reason_data.append({
                'name': reason_name,
                'value': reason_value,
                'count': count
            })
        
        context['reason_data'] = reason_data
        return context