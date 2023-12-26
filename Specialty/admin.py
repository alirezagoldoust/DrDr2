from django.contrib.admin import ModelAdmin, register
from .models import speciality, doctor, patient, comment, reserve
# Register your models here.

@register(speciality)
class speciality_admin(ModelAdmin):
    list_display =['Name']

@register(doctor)
class doctor_admin(ModelAdmin):
    list_display =['Name', 'Specialty']
    search_fields =('Specialty__Name',)

@register(patient)
class patient_admin(ModelAdmin):
    list_display =['Name']

@register(reserve)
class reserve_admin(ModelAdmin):
    list_filter =['Time']
    search_fields =['Doctor__Name']

@register(comment)
class comment_admin(ModelAdmin):
    list_display=['User','Doctor', 'Comment']


