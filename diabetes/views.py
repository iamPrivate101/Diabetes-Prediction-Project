from django.shortcuts import render
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import DiabetesPredictForm
from django.contrib import messages
from diabetes.models import Prediction

from .models import Carausel


# Create your views here.


#carausel
def index(request):
    obj = Carausel.objects.all()
    context = {
        'obj':obj
    }
    return render(request, "diabetes/index.html",context)


def about(request):
    return render(request, "diabetes/about.html")


def blog(request):
    return render(request, "diabetes/blog.html")


def analyze(request):
    return render(request, "diabetes/analyze.html")


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



def predict(request):
    if request.method == "POST":
        form = DiabetesPredictForm(request.POST)
        # loading dataset
        data = pd.read_csv("diabetes.csv")
        # train test split
        X = data.drop("Outcome", axis=1)
        Y = data["Outcome"]
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)
        # Trainning the Model
        model = LogisticRegression()
        model.fit(X_train, Y_train)

        val1 = float(request.POST["pregnancies"])
        val2 = float(request.POST["gulcose"])
        val3 = float(request.POST["blood_pressure"])
        val4 = float(request.POST["skin_thickness"])
        val5 = float(request.POST["insuline"])
        val6 = float(request.POST["bmi"])
        val7 = float(request.POST["diabetes_pedigree"])
        val8 = float(request.POST["age"])

        pred = model.predict([[val1, val2, val3, val4, val5, val6, val7, val8]])
        print(pred)

        result1 = ""
        if pred == [1]:
            result1 = "Positive"
        else:
            result1 = "Negative"

        # ins = Prediction( pregnancies=val1, gulcose =val2 , blood_pressure=val3, skin_thickness=val4,insuline=val5, bmi=val6, diabetes_pedigree=val7, age=val8,result=result1)

        if form.is_valid():
            form.save()
            # ins.save()

            username = form.cleaned_data.get("user")
            messages.success(
                request,
                f"{ username } : Diabetes {result1} ",
                
            )
    else:
        form = DiabetesPredictForm()

    context = {
        "form": form,
    }
    return render(request, "diabetes/predict.html", context)
