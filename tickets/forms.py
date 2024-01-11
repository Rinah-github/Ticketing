from django import forms
from tickets.models import ticket

class CreateTicketForm(forms.ModelForm):
    class Meta:
        model = ticket
        fields = ['title', 'description']

    
class UpdateTicketForm(forms.ModelForm):
    class Meta:
        model = ticket
        fields = ['title', 'description']