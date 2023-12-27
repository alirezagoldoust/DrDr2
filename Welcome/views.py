from django.shortcuts import render, redirect
from django.http.response import HttpResponse, JsonResponse
from Specialty.models import Speciality

# Create your views here.
def welcome(request):
    if request.method == 'POST':
        selected_specialty = request.POST['selected_specialty']
        return redirect('/specialty/' + selected_specialty)
    specialities = Speciality.objects.all()
    return render(request, 'Welcome/wellcome.html', context={'specialities' : specialities})
                                                                