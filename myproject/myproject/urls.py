from django.contrib import admin
from django.urls import path, include
from attendance import views  # Import your views module

urlpatterns = [
    path('', views.user_login, name='login'),  # Set login page as root URL
    path('admin/', admin.site.urls),
    path('attendance/', include('attendance.urls')),
    # Other URL patterns
]
