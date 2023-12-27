from django.db import models

# Create your models here.
class Ticket(models.Model):
    message = models.TextField()

class Reply(models.Model):
    message = models.TextField()
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)


