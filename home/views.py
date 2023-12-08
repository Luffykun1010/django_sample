from django.shortcuts import render
from .models import Departments,Doctors,Booking
# Create your views here.
def home(request):
    return render(request,'home1.html')
def booking(request):
    if request.method == 'POST':
        p_name=request.POST.get('name')
        p_phone=request.POST.get('phone')
        booking_date=request.POST.get('date')
        doc_name=request.POST.get('docname')
        form=Booking.objects.create(p_name=p_name,p_phone=p_phone,doc_name=doc_name,booking_date=booking_date)
        form.save()
        return render(request,'confirmation.html')
    dict_form={

        'doct':Doctors.objects.all()
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
