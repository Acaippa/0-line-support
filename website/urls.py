from django.urls import path, include, re_path
from problems import urls

urlpatterns = [
    path('', include(urls)),
    re_path(r"^accounts/", include("django.contrib.auth.urls")), # Legg dil Django's innebygde registrering for brukere https://realpython.com/django-user-management/
]
