from django.urls import path
from diabetes.views import index

app_name = 'diabetes'
urlpatterns = [
    path('',index,name="index"),
  

]
