from django.urls import path
from .views import list_ticket_reply

urlpatterns = [
    path('', list_ticket_reply)
]