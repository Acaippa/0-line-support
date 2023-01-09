from django.contrib import admin
from django.urls import path
from .views import main_page, card_detail, ticket_page

urlpatterns = [
    path('admin', admin.site.urls),
    path('', main_page),
    path('problem', card_detail),
    path('ticket', ticket_page),
]
