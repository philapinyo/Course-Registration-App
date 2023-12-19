from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
        else:
            messages.warning(request, 'Unable to create account!')
            return redirect('home')
    else:
        form = UserCreationForm()
        return render(request, 'register.html', {'form': form ,
        'title': 'Student Registration'})


def home(request):

    return render(request, 'home.html', context={})


def about(request):
    
    return render(request, 'about.html')

def contact(request):
    
    return render(request, 'contact.html')

# Create your views here.
