from django.urls import path
from .views import LeadUpdateView, LeadListView, LeadCreateView, DashboardView

app_name = 'leads'

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('leads/', LeadListView.as_view(), name='lead_list'),
    path('add/', LeadCreateView.as_view(), name='add_lead'),
    path('leads/edit/<int:pk>/', LeadUpdateView.as_view(), name='edit_lead'),
]