from django.contrib import admin
from django.urls import path
from .views import home, card_detail, ticket, edit_problem, add_problem, add_problem, delete_problem, ticket


urlpatterns = [
    path('admin', admin.site.urls),
    path('', home),
    path('problem/<int:problemId>', card_detail),
    path('ticket/<int:problemId>', ticket),
    path('editproblem/<int:problemId>', edit_problem),
    path('addproblem', add_problem),

    path('editproblem/<int:problemId>', edit_problem),
    path('addproblem', add_problem),

    path('deleteproblem/<int:problemId>', delete_problem),

    path('ticket', ticket),
]
