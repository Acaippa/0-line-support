from django.contrib import admin
from .models import UnderKategori, Kategori, Problem

admin.site.register(Problem)
admin.site.register(UnderKategori)
admin.site.register(Kategori)