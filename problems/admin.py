from django.contrib import admin
from .models import UnderKategori, Kategori, Problem, Ticket, Status

admin.site.register(Problem)
admin.site.register(UnderKategori)
admin.site.register(Kategori)
admin.site.register(Status)

class TicketAdmin(admin.ModelAdmin):
    list_display = ["emne", "email", "status"]

admin.site.register(Ticket, TicketAdmin)