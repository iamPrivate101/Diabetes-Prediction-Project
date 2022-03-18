from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created { username }')
            return redirect('diabetes:index')
    else:
        form = UserRegisterForm()
    context = {
        'form':form,
        
    }

    return render(request, 'users/register.html', context)


def login(request):
 
    context = {
        
    }

    return render(request, 'users/login.html', context)
