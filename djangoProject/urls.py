from django.urls import path
from app_name.views import PhoneListView, PhoneDetailView

urlpatterns = [
    path('', PhoneListView.as_view(), name='phone_list'),
    path('<str:slug>/', PhoneDetailView.as_view(), name='phone_detail'),
]