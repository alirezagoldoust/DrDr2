from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from .models import Speciality, Doctor, Patient, Reserve
from datetime import datetime
# Create your views here.

def list_specialty(request):
    specialities = Speciality.objects.all()
    specialities_json = {'Specialty':specialities}
    return render(request, 'Specialty/specialty.html', specialities_json)

def list_doctor(request, speciality_name):
    doctors = Doctor.objects.filter(specialty__name = speciality_name)
    return render(request, 'Logy/logy.html', context={'doctors':doctors, 'specialty':speciality_name})

def reserve(request, speciality_name, doctor_id):

    if request.method == 'GET':
        # Sending the selected doctors data to html
        dr = Doctor.objects.get(code=doctor_id)
        return render(request, 'Detail/detail.html', context={'doctor':dr})

    if request.method == 'POST':
        # Getting data about reservation
        input = {
            'name' : request.POST['name'] + ' ' + request.POST['lastname'],
            'ni'   : request.POST['ni'],
            'age'  : request.POST['age'],
            'date' : request.POST['date'],
            'time' : request.POST['time'],
        }
        selected_doctor=Doctor.objects.get(code=doctor_id)

        # Checking possibilty of reservation
        if not Reserve.objects.filter(doctor=selected_doctor, date = input['date'], time=input['time']).exists():
            # Checking if user exist in database or making it
            if not Patient.objects.filter(national_id=input['ni']).exists():
                Patient.objects.create(name=input['name'], age=input['age'], national_id=input['ni'])
            selected_patient = Patient.objects.get(national_id=input['ni'])
            Reserve.objects.create(
                bimar=selected_patient,
                doctor=selected_doctor,
                date=input['date'],
                time=input['time']
            )
            return render(request, 'Specialty/reserve.html', {'Success' : True})
        else:
            return render(request, 'Specialty/reserve.html', {'Success' : False})