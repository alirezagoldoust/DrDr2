from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from Specialty.models import speciality, doctor

# Create your views here.
def welcome(request):
    if request.method == 'POST':
        selected_specialty = request.POST['selected_specialty']
        doctors = doctor.objects.filter(Specialty__Name=selected_specialty)
        return render(request, 'Logy/logy.html', context={'doctors':doctors})
    specialities = speciality.objects.all()
    return render(request, 'Welcome/wellcome.html', context={'specialities' : specialities})
                                                                
# def goto_specialty(request):
    # return HttpResponse(selected_specialty)