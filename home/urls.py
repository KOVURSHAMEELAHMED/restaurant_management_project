from django.urls import path
from .views import FAQListView

urlpatterns = [
    # ... your other paths ...
    path('api/faqs/', FAQListView.as_view(), name='faq-list'),
]