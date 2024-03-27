from django.shortcuts import  get_object_or_404
from django.http import HttpResponse
from .forms import TestReportForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import PatientRegistrationForm, PatientProfileForm
from .models import Patient,TestReport
from django.contrib.auth import authenticate, login,logout
from .forms import PatientLoginForm

from django.contrib.auth.decorators import login_required





def patient_logout(request):
    logout(request)
    return redirect('patient_login')  # Redirect to the login page after logout




@login_required
def user_report_panel(request):
    user = request.user
    reports = TestReport.objects.filter(patient=user.patient)
    return render(request, 'user_report_panel/user_report_panel.html', {'user': user, 'reports': reports})


def patient_login(request):
    if request.method == 'POST':
        form = PatientLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('user_report_panel')  # Redirect to the user report panel
            else:
                form.add_error(None, "Invalid username or password.")
    else:
        form = PatientLoginForm()
    return render(request, 'patients/patient_login.html', {'form': form})

def patient_register(request):
    if request.method == 'POST':
        user_form = PatientRegistrationForm(request.POST)
        profile_form = PatientProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            login(request, user)
            return redirect('home')  # Redirect to the home page or any other desired URL
    else:
        user_form = PatientRegistrationForm()
        profile_form = PatientProfileForm()
    return render(request, 'patients/patient_register.html', {'user_form': user_form, 'profile_form': profile_form})


def home(request):
    if request.method=='POST':
        name=request.POST['name']
        img = request.POST['file']
        testreport=TestReport(name=name,uploaded_at=img)
        testreport.save()

        # print(name,email,msg)
        return redirect('/')
    testreport = TestReport.objects.all()[::-1]
    context = {'testreport': testreport}
    # print(allpost)
    return render(request, 'patients/index.html', context)


def upload_report(request):
    if request.method == 'POST':
        form = TestReportForm(request.POST, request.FILES)
        print(request.POST)  # Print POST data for debugging
        print(request.FILES)  # Print uploaded files for debugging

        if form.is_valid():
            # Get cleaned and validated data

            patient = form.cleaned_data['patient']
            report_file = form.cleaned_data['report_file']
            # Save the appointment
            testreport = TestReport(patient=patient, report_file=report_file)
            testreport.save()

            return redirect('user_report_panel')  # Redirect to success page after saving
    else:
        form = TestReportForm()
    patients = Patient.objects.all()
    return render(request, 'user_report_panel/upload_report.html', {'form': form, 'patients': patients})



def view_reports(request):
    reports = TestReport.objects.filter(patient=request.user.patient)
    return render(request, 'user_report_panel/view_reports.html', {'reports': reports})

def delete_report(request, report_id):
    report = get_object_or_404(TestReport, id=report_id)
    if request.method == 'POST':
        report.delete()
        return redirect('view_reports')
    return render(request, 'user_report_panel/delete_report.html', {'report': report})
