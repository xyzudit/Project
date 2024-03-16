from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from .forms import AttendanceForm, LoginForm  # Import LoginForm
from django.contrib import messages

def home(request):
    if request.method == 'POST':
        form = AttendanceForm(request.POST, request.FILES)
        if form.is_valid():
            attendance = form.save(commit=False)
            is_present = request.POST.get('present', False)
            if is_present:
                attendance.present = True
            attendance.save()
            messages.success(request, 'Attendance marked successfully!')
            return render(request, 'attendance/success.html')
        else:
            error_message = "Failed to mark attendance. Please check the form fields."
            for field, errors in form.errors.items():
                error_message += f"\n{field}: {', '.join(errors)}"
            messages.error(request, error_message)
    else:
        form = AttendanceForm()
    return render(request, 'attendance/home.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password.', extra_tags='red')
        else:
            messages.error(request, 'Invalid form submission. Please try again.', extra_tags='red')
    else:
        form = AuthenticationForm()
    return render(request, 'attendance/login.html', {'form': form})