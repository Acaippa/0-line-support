from django.forms import ModelForm

from .models import Problem, Ticket

class ProblemForm(ModelForm): # Form laget av problem-modellen som vi kan spesifisere hvilke felt som skal vises.
    class Meta:
        model = Problem
        fields = ["tittel", "beskrivelse", "guide", "dato_postet", "kategori", "under_kategori"]

class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ["email", "emne", "melding"]