from django.db import models

class Ticket:
    emne = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    detalj = models.TextField(max_length=1000)

    oppdragstaker