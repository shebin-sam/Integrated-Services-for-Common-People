from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, SignInForm
from .forms import ServiceRegistrationForm
from .models import Service,SERVICE_TYPES
from .forms import ContactForm
from django.contrib.auth import logout
@login_required
def service_registration(request):
    if request.method == 'POST':
        form = ServiceRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('service_list')
    else:
        form = ServiceRegistrationForm()
    return render(request, 'service_registration.html', {'form': form,'username': request.user.username})

@login_required
def service_list(request):
    services = Service.objects.all()
    service_type = request.GET.get('service_type')
    if service_type:
        services = services.filter(service_type=service_type)
    return render(request, 'service_list.html', {'services': services, 'service_types': SERVICE_TYPES,'username': request.user.username})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def signin(request):
    if request.method == 'POST':
        form = SignInForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = SignInForm()
    return render(request, 'signin.html', {'form': form})



@login_required
def profile(request):
    return render(request, 'profile.html',{'username': request.user.username})

@login_required
def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_success')  # Redirect to a success page or another view
    else:
        form = ContactForm()
    return render(request, 'index.html', {'form': form, 'username': request.user.username})


def contact_success(request):
    return render(request, 'contact_success.html',{'username': request.user.username})

def index(request):
    return render(request, 'home.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('')