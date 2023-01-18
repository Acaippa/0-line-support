from django.db import models
import datetime
from random import randint

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
    under_kategori = models.ForeignKey(UnderKategori, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.navn


class Problem(models.Model):
    problem_id = models.IntegerField(default=generate_id, editable=False)
    tittel = models.CharField(max_length=200, primary_key=True)
    beskrivelse = models.CharField(max_length=1000)
    guide = models.TextField(max_length=20000)
    dato_postet = models.DateField(default=datetime.date.today)
    kategori = models.ForeignKey(Kategori, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.tittel
