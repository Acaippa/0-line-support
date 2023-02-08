from django.contrib import admin
from django.urls import path
from .views import main_page, card_detail, ticket_page, edit_problem_page, edit_problem_backend, add_problem, add_problem_backend, delete_problem, filter_backend, ticket_backend


urlpatterns = [
    path('admin', admin.site.urls),
    path('', main_page),
    path('problem/<int:problemId>', card_detail),
    path('ticket/<int:problemId>', ticket_page),
    path('editproblem/<int:problemId>', edit_problem_page),
    path('addproblem', add_problem),

    path('editproblembackend/<int:problemId>', edit_problem_backend),
    path('addproblembackend', add_problem_backend),

    path('deleteproblem/<int:problemId>', delete_problem),

    path('filter', filter_backend),

    path('ticketbackend', ticket_backend),
]
