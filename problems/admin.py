from django.contrib import admin
from .models import UnderKategori, Kategori, Problem, Ticket, State

admin.site.register(Problem)
admin.site.register(UnderKategori)
admin.site.register(Kategori)
admin.site.register(Ticket)
admin.site.register(State)
