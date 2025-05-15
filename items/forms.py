# items/forms.py

from django import forms
from .models import LostItem

class LostItemForm(forms.ModelForm):
    class Meta:
        model = LostItem
        fields = ['title', 'description', 'date_lost', 'location', 'status', 'image']
