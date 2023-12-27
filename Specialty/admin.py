from django.contrib.admin import ModelAdmin, register
from .models import Speciality, Doctor, Patient, Comment, Reserve
# Register your models here.

@register(Speciality)
class SpecialityAdmin(ModelAdmin):
    list_display =['name']

@register(Doctor)
class DoctorAdmin(ModelAdmin):
    list_display =['name', 'specialty']
    search_fields =('specialty__Name',)

@register(Patient)
class PatientAdmin(ModelAdmin):
    list_display =['name']

@register(Reserve)
class ReserveAdmin(ModelAdmin):
    list_filter =['time']
    search_fields =['doctor__Name']

@register(Comment)
class CommentAdmin(ModelAdmin):
    list_display=['user','doctor', 'comment']


