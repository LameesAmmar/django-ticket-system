from .models import Ticket
from django.forms import ModelForm
from users.models import User

class CreateTicketForm(ModelForm):
    class Meta:  # Corrected from Mete to Meta
        model = Ticket
        fields = ['ticket_title', 'ticket_description']



class UpdateTicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields= ['ticket_title','ticket_description']


class AssignTicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields= ['engineer']

class solvedTicketForm (ModelForm):
    class Meta:
        model = Ticket
        fields= ['resolution_steps']

