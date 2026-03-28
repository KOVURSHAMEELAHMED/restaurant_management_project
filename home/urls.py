from django.urls import path
from .views import DailySpecialsListView

urlpatterns = [
    path('daily-specials/', DailySpecialsListView.as_view(), name='daily-specials'),
]