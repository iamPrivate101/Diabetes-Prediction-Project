from django.shortcuts import render
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Create your views here.

def index(request):
    return render(request, 'diabetes/index.html')

def about(request):
    return render(request, 'diabetes/about.html')

def blog(request):
    return render(request, 'diabetes/blog.html')

def analyze(request):
    return render(request,'diabetes/analyze.html')


def result(request):
    #loading dataset
    data = pd.read_csv("diabetes.csv")
    #train test split
    X = data.drop("Outcome", axis=1)
    Y = data['Outcome']
    X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.2)
    #Trainning the Model
    model = LogisticRegression()
    model.fit(X_train,Y_train)

    val1 = float(request.GET['pregnancies'])
    val2 = float(request.GET['gulcose'])
    val3 = float(request.GET['blood_pressure'])
    val4 = float(request.GET['skin_thickness'])
    val5 = float(request.GET['insuline'])
    val6 = float(request.GET['bmi'])
    val7 = float(request.GET['diabetes_pedigree'])
    val8 = float(request.GET['age'])

    pred = model.predict([[val1,val2,val3,val4,val5,val6,val7,val8]])

    result1 = ""
    if pred == [1]:
        result1 = "Positive"
    else:
        result1 = "Negative"



    return render(request,"diabetes/analyze.html",{'result2':result1})







