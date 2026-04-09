from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer_name', 'customer_email', 'customer_phone', 'customer_notes']
        widgets = {
            'customer_notes': forms.Textarea(attrs={
                'rows': 4,
                'placeholder': 'Any special instructions? (e.g., "Leave at door", "Allergic to nuts", "Extra napkins please")'
            }),
        }
        labels = {
            'customer_notes': 'Special Instructions or Notes'
        }