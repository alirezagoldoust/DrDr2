from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from .models import speciality, doctor, patient, reserve
from datetime import datetime
# Create your views here.

def List_Specialty(request):
    specialities = speciality.objects.all()
    specialities_json = {'Specialty':specialities}
    return render(request, 'Specialty/specialty.html', specialities_json)

def List_Doctor(request, speciality_name):
    doctors = doctor.objects.filter(Specialty__Name = speciality_name)
    return render(request, 'Logy/logy.html', context={'doctors':doctors, 'specialty':speciality_name})

def Reserve(request, speciality_name, doctor_id):

    if request.method == 'GET':
        # Sending the selected doctors data to html
        dr = doctor.objects.get(Code=doctor_id)
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
        selected_doctor=doctor.objects.get(Code=doctor_id)

        # Checking possibilty of reservation
        if not reserve.objects.filter(Doctor=selected_doctor, Date = input['date'], Time=input['time']).exists():
            # Checking if user exist in database or making it
            if not patient.objects.filter(National_id=input['ni']).exists():
                patient.objects.create(Name=input['name'], Age=input['age'], National_id=input['ni'])
            selected_patient = patient.objects.get(National_id=input['ni'])
            reserve.objects.create(
                Bimar=selected_patient,
                Doctor=selected_doctor,
                Date=input['date'],
                Time=input['time']
            )
            return render(request, 'Specialty/reserve.html', {'Success' : True})
        else:
            return render(request, 'Specialty/reserve.html', {'Success' : False})