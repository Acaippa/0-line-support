from django.db import models
import datetime
from random import randint
from website.settings import*

from django.forms import ModelForm


def get_rand():
    return randint(0, 9)

def generate_id():
    return f"{get_rand()}{get_rand()}{get_rand()}{get_rand()}{get_rand()}{get_rand()}"

class UnderKategori(models.Model):
    navn = models.CharField(max_length=70)
    farge = models.CharField(max_length=6)

    def __str__(self):
        return self.navn


class Kategori(models.Model):
    navn = models.CharField(max_length=50, primary_key=True)
    farge = models.CharField(max_length=6)

    def __str__(self):
        return self.navn


class Problem(models.Model):
    problem_id = models.IntegerField(default=generate_id, editable=False, primary_key=True)
    tittel = models.CharField(max_length=200)
    beskrivelse = models.CharField(max_length=1000)
    guide = models.TextField(max_length=20000)
    dato_postet = models.DateField(default=datetime.date.today)
    kategori = models.ForeignKey(Kategori, on_delete=models.DO_NOTHING)
    under_kategori = models.ForeignKey(UnderKategori, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.tittel
    

class ProblemForm(ModelForm): # Form laget av problem-modellen som vi kan spesifisere hvilke felt som skal vises.
    class Meta:
        model = Problem
        fields = ["tittel", "beskrivelse", "guide", "dato_postet", "kategori", "under_kategori"]

class State(models.Model):
    navn = models.CharField(max_length=50)

    def __str__(self):
        return self.navn
    
    
class Ticket(models.Model):
    email = models.EmailField()
    emne = models.CharField(max_length=200)
    melding = models.TextField(max_length=1500)
    state = models.ForeignKey(State, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.emne}, {self.email}"

class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ["email", "emne", "melding"]


