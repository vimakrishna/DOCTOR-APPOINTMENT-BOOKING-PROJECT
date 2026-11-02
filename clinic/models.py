from django.db import models

# Create your models here.

class DoctorDb(models.Model):
    Doctor_name = models.CharField(max_length=100)
    Specialization = models.CharField(max_length=100)
    Experience = models.PositiveIntegerField()
    Hospital = models.CharField(max_length=150)
    Consultation_fee = models.PositiveIntegerField()
    Available = models.BooleanField(default=True)

    def __str__(self):
        return self.Doctor_name

class AppointmentDb(models.Model):
    Patient_name = models.CharField(max_length=100)
    Phone = models.CharField(max_length=20)
    Doctor_id = models.IntegerField()
    Appointment_date = models.DateField()
    Token_number = models.PositiveIntegerField(editable=False,null=True)
    Appointment_time = models.TimeField(editable=False,null=True)
    Problem = models.TextField()                                       
    Status = models.CharField(max_length=200,default="pending")
    prescription = models.TextField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Patient_name
    