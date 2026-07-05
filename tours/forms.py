from django import forms
from .models import ContactMessage


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ["name", "email", "phone", "package_interest", "message"]
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Your full name", "class": "field-input"}),
            "email": forms.EmailInput(attrs={"placeholder": "you@example.com", "class": "field-input"}),
            "phone": forms.TextInput(attrs={"placeholder": "+255 ...", "class": "field-input"}),
            "package_interest": forms.TextInput(attrs={"placeholder": "e.g. 5 Days Northern Circuit Safari", "class": "field-input"}),
            "message": forms.Textarea(attrs={"placeholder": "Tell us about your dream safari...", "class": "field-input", "rows": 5}),
        }
