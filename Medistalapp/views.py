from django.shortcuts import render, redirect
from Medistalapp.models import Company, Patient, Appointment


# Create your views here.
def index(request):
    return render(request, 'index.html')


def starter(request):
    return render(request, 'starter-page.html')


def about(request):
    return render(request, 'about.html')


def services(request):
    return render(request, 'Services.html')


def departments(request):
    return render(request, 'departments.html')


def doctors(request):
    return render(request, 'doctors.html')


def Contacts(request):
    if request.method == 'POST':
        contact = Company(name=request.POST['name'],
                          email=request.POST['email'],
                          message=request.POST['message'],
                          phone=request.POST['phone'],
                          staff=request.POST['staff'])

        contact.save()
        return redirect('/contacts')

    else:
        return render(request, 'contacts.html')


def patients(request):
    if request.method == 'POST':
        patient = Patient(fullname=request.POST['name'],
                          email=request.POST['email'],
                          medicalhistory=request.POST['medical history'],
                          age=request.POST['age'])

        patient.save()
        return redirect('/patients')

    else:
        return render(request, 'patients.html')


def appointment(request):
    if request.method == 'POST':
        appointment = Appointment(name=request.POST['name'],
                                  email=request.POST['email'],
                                  phone=request.POST['phone'],
                                  date=request.POST['date'],
                                  department=request.POST['department'],
                                  doctor=request.POST['doctor'],
                                  message=request.POST['message'], )

        appointment.save()
        return redirect('/appointments')

    else:
        return render(request, 'appointment.html')

def show(request):
    data = Appointment.objects.all()
    return render(request,'Show.html',{'appointment':data})

def delete(request,id):
    myappointment = Appointment.objects.get(id=id)

    myappointment.delete()
    return redirect('/show')
