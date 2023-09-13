from django.shortcuts import render
from .models import Departments,Doctors
from .forms import BookingForm
# Create your views here.
def home(request):
    return render(request,'home1.html')
def booking(request):
    if request.method == 'POST':
        form=BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'confirmation.html')
    form=BookingForm()
    dict_form={
        'form': form
    }
    return render(request,'booking.html',dict_form)
def department(request):
    dict_dept={
        'dept':Departments.objects.all()
    }
    return render(request,'departments.html',dict_dept)
def doctor(request):
    dict_doct={
        'doct':Doctors.objects.all()
    }
    return render(request,'doctors.html',dict_doct)
def contact(request):
    return render(request,'contact.html')
def hafeez(request):
    dict_doct={
        'doct':Doctors.objects.all()
    }
    return render(request,'drhafeez.html',dict_doct)
def gynecologist(request):
    dict_doct={
        'doct':Doctors.objects.all()
    }
    return render(request,'gynecologist.html',dict_doct)
def surgeon(request):
    dict_doct={
        'doct':Doctors.objects.all()
    }
    return render(request,'surgery.html',dict_doct)
