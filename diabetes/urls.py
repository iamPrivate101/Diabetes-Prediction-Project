from django.urls import path
from diabetes import views as diabetes_views

app_name = 'diabetes'
urlpatterns = [
    path('',diabetes_views.index,name="index"),
    path('about/',diabetes_views.about,name="about"),
    path('blog/',diabetes_views.blog,name="blog"),


  

]
