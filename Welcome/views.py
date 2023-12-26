from django.shortcuts import render
from Specialty.models import speciality

# Create your views here.
def welcome(request):
    specialities = speciality.objects.all()
    print(specialities)
    return render(request, 'Welcome/wellcome.html', context={'specialities' : specialities})