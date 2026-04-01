from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import SampleForm
from django.core.mail import send_mail

def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'accounts/login.html', {'error': 'Invalid credentials'})

    return render(request, 'accounts/login.html')


def user_logout(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def dashboard(request):
    return render(request, 'accounts/home.html')
def sample_form(request):
    form = SampleForm()

    if request.method == "POST":
        form = SampleForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            return render(request, 'accounts/result.html', {
                'name': name,
                'email': email,
                'message': message
            })

    return render(request, 'accounts/form.html', {'form': form})
def send_email(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        send_mail(
            subject=f"Message from {name}",
            message=message,
            from_email=email,
            recipient_list=['admin@gmail.com'],
        )

        return render(request, 'accounts/success.html')

    return render(request, 'accounts/email.html')