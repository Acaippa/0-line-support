from django.urls import path, include
from pages import urls

urlpatterns = [
    path('', include(urls)),
]
