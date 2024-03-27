from django import forms
from .models import TestReport
from django.contrib.auth.models import User
from .models import Patient
from django.contrib.auth.forms import AuthenticationForm


class PatientLoginForm(AuthenticationForm):
    class Meta:
        fields = ['username', 'password']

class PatientRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class PatientProfileForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['name', 'age']



class TestReportForm(forms.ModelForm):
    class Meta:
        model = TestReport
        fields = ['patient','report_file']


