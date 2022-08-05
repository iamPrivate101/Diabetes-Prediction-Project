from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Prediction(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pregnancies = models.DecimalField(max_digits=10, decimal_places=2)
    gulcose = models.DecimalField(max_digits=10, decimal_places=2)
    blood_pressure = models.DecimalField(max_digits=10, decimal_places=2)
    skin_thickness = models.DecimalField(max_digits=10, decimal_places=2)
    insuline = models.DecimalField(max_digits=10, decimal_places=2)
    bmi = models.DecimalField(max_digits=10, decimal_places=4)
    diabetes_pedigree = models.DecimalField(max_digits=10, decimal_places=4)
    age = models.DecimalField(max_digits=10, decimal_places=2)
    date_posted = models.DateTimeField(default=timezone.now)
    result = models.CharField(max_length=255)

    def __str__(self) :
        return f"{self.user} Report"

    class Meta:
        verbose_name = "Report"
        verbose_name_plural = "Reports"
    

    
class Carausel(models.Model):
    image = models.ImageField(upload_to='pics/%y/%m/%d')
    title = models.CharField(max_length=150)
    sub_title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

