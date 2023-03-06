from django.db import models
import datetime
from random import randint
from colorfield.fields import ColorField


from django.forms import ModelForm


def generate_id():
    return randint(0, 100000)


class UnderKategori(models.Model):
    navn = models.CharField(max_length=70)
    farge = ColorField(default="#ffffff")
    tekst_farge = ColorField(default="#ffffff")

    def __str__(self):
        return self.navn


class Kategori(models.Model):
    navn = models.CharField(max_length=50, primary_key=True)
    farge = ColorField(default="#ffffff")
    tekst_farge = ColorField(default="#ffffff")

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

class Status(models.Model):
    navn = models.CharField(max_length=50)

    def __str__(self):
        return self.navn

def get_default_status():
    open_state = Status.objects.filter(navn="Åpen")
    
    if open_state.exists():
        return open_state[0]
    
    return ""
    
class Ticket(models.Model):
    email = models.EmailField()
    emne = models.CharField(max_length=200)
    melding = models.TextField(max_length=1500)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, null=True, blank=True, default=get_default_status) # Gjør standardstaten til "Åpen"

    def __str__(self):
        return f"{self.emne}, {self.email}"



