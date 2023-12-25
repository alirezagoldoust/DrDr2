from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from .models import speciality, doctor, patient
# Create your views here.

def List_Specialty(request):
    specialities = speciality.objects.all()
    specialities_json = {'Specialty':specialities}
    return render(request, 'Specialty/index.html', specialities_json)

def List_Doctor(request, speciality_name):
    doctors = doctor.objects.filter(Specialty__Name = speciality_name)
    return render(request, 'Logy/logy.html', {'doctors':doctors})

def Reserve(request, speciality_name, doctor_id):
    if request.method == 'GET':
        dr = doctor.objects.get(Code=doctor_id)
        return render(request, 'Specialty/detail.html', {'doctor':dr})
    if request.method == 'POST':
        input = []
        input.append({'name' : request.POST['name']})
        input.append({'ni' : request.POST['ni']})
        input.append({'lastname' : request.POST['lastname']})
        input.append({'age' : request.POST['age']})
        input.append({'time' : request.POST['time']})
        new_patient =  patient(input['name'] + input['lastname'], input['age']),
        patient.objects.Create(new_patient)
        Reserve.objects.Create(
            patient(),
            doctor(),
            request.POST['time'],
        )
        return JsonResponse(input, safe=False)