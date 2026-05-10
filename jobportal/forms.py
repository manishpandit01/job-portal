from django import forms
from jobportal.models import Contact, JobApplication

class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields="__all__"
    
class JobApplicationForm(forms.ModelForm):
    class Meta:
        model=JobApplication
        fields=[
            "name",
            "email",
            "portfolio_website",
            "resume",
            "cover_letter",
        ]