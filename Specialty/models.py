from django.db import models
# Create your models here.

class speciality(models.Model):
    Name=models.CharField(max_length=100)
    def __str__(self):
        return self.Name

class doctor(models.Model):
    Name=models.CharField(max_length=200)
    Specialty = models.ForeignKey(speciality, on_delete=models.CASCADE)
    Sum_Scores=models.FloatField(default=0, editable=False)
    Count_Scores=models.FloatField(default=0, editable=False)
    Average_Score=models.FloatField(default=0, editable=False)
    Code=models.CharField(max_length=6, unique=True)
    Phone_number=models.CharField(max_length=11)
    Visit_cost=models.IntegerField()
    def __str__(self):
        return self.Name


class patient(models.Model):
    Name=models.CharField(max_length=200)
    Age=models.PositiveIntegerField()
    National_id=models.IntegerField()
    def __str__(self):
        return self.Name

class reserve(models.Model):
    Bimar = models.ForeignKey(patient, on_delete=models.CASCADE)
    Doctor = models.ForeignKey(doctor, on_delete=models.CASCADE)
    Time = models.TimeField()
    Date = models.DateField()
    def __str__(self):
        return f'{self.Bimar} - {self.Doctor} in {self.Time}'

class comment(models.Model):
    User = models.CharField(max_length=100)
    Comment = models.TextField()
    Doctor = models.ForeignKey(doctor, on_delete=models.CASCADE)
    def __str__(self):
        return self.Comment
