from django.contrib import admin
from home.models import Vehicle 
# Register your models here.

class VehicleAdmin(admin.ModelAdmin):
    list_display = ['vehicle_reg_no','vehicle_color','vehicle_brand','vehicle_image','vehicle_menufatured_date']

admin.site.register(Vehicle,VehicleAdmin) 