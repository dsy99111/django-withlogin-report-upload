from django.db import models
from django.contrib.auth.models import User

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.user.username

class TestReport(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.SET_NULL, null=True, blank=True,
                                related_name='testreports_as_doctor')
    report_file = models.FileField(upload_to='image/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.patient:
            return f"Test Report for {self.patient.user.username}"
        else:
            return "Test Report (No patient assigned)"
