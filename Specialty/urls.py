from django.urls import path
from .views import list_doctor, list_specialty, reserve

urlpatterns = [
    path('', list_specialty),
    path('<str:speciality_name>/', list_doctor),
    path('<str:speciality_name>/<str:doctor_id>/', reserve),
]

