from django.db import models

# Create your models here.

BRANDS = {
    ('HN','Honda'),
    ('TY','Toyota'),
    ('MD','Mercedes'),
    ('BMW','BMD')
}
class Vehicle(models.Model):

    vehicle_reg_no = models.CharField(max_length=16)
    vehicle_color  = models.CharField(max_length=100)
    vehicle_brand  = models.CharField(max_length=32,choices=BRANDS)
    vehicle_image  = models.ImageField(upload_to='media/')
    vehicle_menufatured_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.vehicle_reg_no
    