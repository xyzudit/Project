from django import forms
from .models import Attendance
from django.contrib.auth.forms import AuthenticationForm

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['employee', 'location'] 

class LoginForm(AuthenticationForm):
    class Meta:
        fields = ['username', 'password']
