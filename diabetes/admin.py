from django.contrib import admin
from .models import Prediction, Carausel, DiabetesTypes
# Register your models here.

admin.site.register(Prediction)
admin.site.register(Carausel)
admin.site.register(DiabetesTypes)

