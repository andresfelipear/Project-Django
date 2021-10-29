from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.forms import UserCreationForm,  AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from .forms import BreakfastForm
from .models import Todo, Breakfast
from django.utils import timezone
from django.contrib.auth.decorators import login_required

# Create your views here.
def signupuser(request):
    if request.method == 'GET':
        return render(request, 'todo/signup.html', { 'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:

            try:
                user = User.objects.create_user(request.POST['username'],"", request.POST['password1'])
                user.save()
                login(request,user)
                return redirect('breakfasts')

            except IntegrityError:
                return render(request, 'todo/signup.html', {'form':UserCreationForm(), 'errMsg':"The username already exist. try another one!"})
            
        else:
            return render(request, 'todo/signup.html', {'form':UserCreationForm(), 'errMsg':"The password and verification are diferents, try again!"})

@login_required
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')


def home(request):
    return render(request, 'todo/home.html')

def loginuser(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return render(request,'todo/home.html', {"msg":"You are already authenticated!!"})
        else:
            return render(request, 'todo/login.html', { 'form': AuthenticationForm()})
    else:
        user = authenticate(
            request,
            username=request.POST['username'], 
            password=request.POST['password1']
        )

        if user is None:
            return render(request, 'todo/login.html', {'form': AuthenticationForm(), "errMsg":'Username and password are incorrect'})
        elif user.is_superuser:
            login(request,user)
            return redirect('breakfasts')
        else:
            login(request,user)
            return render(request,'todo/home.html', {"msg":"Thanks for login. You can start buying!"})
            

@login_required
def breakfasts(request):
    breakfasts = Breakfast.objects.filter(user=request.user)
    return render(request, 'todo/breakfasts.html', {'todos':breakfasts})

@login_required
def create(request):
    if request.method == 'GET':
        return render(request, 'todo/create.html', { 'form': BreakfastForm()})
    else:
        try:
            form = BreakfastForm(request.POST)
            newtodo = form.save()
            newtodo.user = request.user
            newtodo.save()
            return redirect('breakfasts')
        except ValueError:
            render(request, "todo/create.html",{ 'form': BreakfastForm(), 'errMsg':'Bad data passed in. try again'})

@login_required
def view(request, breakfast_id):
    breakfast = get_object_or_404(Breakfast,pk=breakfast_id,user=request.user)
    if request.method == "GET":
        form = BreakfastForm(request.POST, instance=breakfast) ####
        return render(request, 'todo/view.html',{'breakfast':breakfast, 'form':form})
    else:
        try:
            form = BreakfastForm(request.POST, instance=breakfast)
            form.save()
            return redirect('breakfasts')
        except ValueError:
            return render(request, 'todo/view.html', {'breakfast':breakfast, 'form':form, 'errMsg':'Bad information...'} )


@login_required
def delete(request, breakfast_id):
    breakfast = get_object_or_404(Breakfast,pk=breakfast_id,user=request.user)
    if request.method == 'POST':
        breakfast.delete()
        return redirect('breakfasts')

def handler404(request, exception):
    return render(request, '404.html', status=404)
