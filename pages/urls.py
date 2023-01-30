from django.contrib import admin
from django.urls import path
from .views import main_page, card_detail, ticket_page, edit_problem_page, edit_problem_backend


urlpatterns = [
    path('admin', admin.site.urls),
    path('', main_page),
    path('problem/<int:problemId>', card_detail),
    path('ticket/<int:problemId>', ticket_page),
    path('editproblem/<int:problemId>', edit_problem_page),

    path('editproblembackend/<int:problemId>', edit_problem_backend)
]
