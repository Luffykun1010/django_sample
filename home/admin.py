from django.contrib import admin
from .models import Doctors,Departments,Booking 
# Register your models here.
admin.site.register(Departments)
admin.site.register(Doctors)
class BookingAdmin(admin.ModelAdmin):
    list_display=('id','p_name','p_phone','doc_name','booking_date','booked_on')
admin.site.register(Booking,BookingAdmin)