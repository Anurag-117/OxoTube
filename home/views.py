from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import CustomUserCreationForm, LoginForm
from django.contrib.auth.decorators import login_required
from .models import VideoItem


def handler404(request, exception):
    return render(request, 'home/404.html', status = 404)


def handler500(request, *args, **argv):
    return render(request, 'home/500.html', status=500)


@login_required()
def home_view(request):
    videos = VideoItem.objects.all()
    context = {'videos': videos}
    return render(request, 'home/videoCatalog.html', context)


def signup_view(request):
    signup_form = CustomUserCreationForm(request.POST or None)
    if request.method == 'POST':
        if signup_form.is_valid():
            print('form valid')
            signup_form.save()
            '''
                If successfully created account let the user sign in
            '''
            messages.success(request, 'Account Successfully Created.')
            form = LoginForm()
            return render(request, 'home/signin.html', {'form': form})
        else:
            print('invalid form')
    return render(request, 'home/signup.html', {'signup_form': signup_form})


def signin_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        userEmail = request.POST['userEmail']
        password = request.POST['password']
        user = authenticate(username=userEmail, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('home:videosPage')
        else:
            messages.error(request, 'username or password incorrect')
            return redirect('home:logInPage')
    else:
        form = LoginForm()
    return render(request, 'home/signin.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home:signUpPage')


