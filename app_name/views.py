from django.views.generic import ListView, DetailView
from app_name.models import Phone

class PhoneListView(ListView):
    model = Phone
    template_name = 'phone_list.html'

class PhoneDetailView(DetailView):
    model = Phone
    template_name = 'phone_detail.html'
    slug_field = 'slug'