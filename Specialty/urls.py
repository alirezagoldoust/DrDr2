from django.urls import path
from .views import List_Doctor, List_Specialty, Reserve

urlpatterns = [
    path('', List_Specialty),
    path('<str:speciality_name>/', List_Doctor),
    path('<str:speciality_name>/<str:doctor_id>/', Reserve),
]

