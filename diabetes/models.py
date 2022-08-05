from django.db import models
from django.contrib.auth.models import User

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
    result = models.CharField(max_length=255)

    

    
class Carausel(models.Model):
    image = models.ImageField(upload_to='pics/%y/%m/%d')
    title = models.CharField(max_length=150)
    sub_title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

