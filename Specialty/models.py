from django.db import models
# Create your models here.

class Speciality(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Doctor(models.Model):
    name=models.CharField(max_length=200)
    specialty = models.ForeignKey(Speciality, on_delete=models.CASCADE)
    sum_Scores=models.FloatField(default=0, editable=False)
    count_Scores=models.FloatField(default=0, editable=False)
    average_Score=models.FloatField(default=0, editable=False)
    code=models.CharField(max_length=6, unique=True)
    phone_number=models.CharField(max_length=11)
    visit_cost=models.IntegerField()
    def __str__(self):
        return self.name


class Patient(models.Model):
    name=models.CharField(max_length=200)
    age=models.PositiveIntegerField()
    national_id=models.IntegerField()
    def __str__(self):
        return self.name

class Reserve(models.Model):
    bimar = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    time = models.TimeField()
    date = models.DateField()
    def __str__(self):
        return f'{self.bimar} - {self.doctor} in {self.time}'

class Comment(models.Model):
    user = models.CharField(max_length=100)
    comment = models.TextField()
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    def __str__(self):
        return self.comment
