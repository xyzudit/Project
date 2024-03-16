from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Attendance

class AttendanceAdmin(admin.ModelAdmin):
    def display_present(self, obj):
        if obj.present:
            return mark_safe('<span style="color:green">&#10004;</span>')  # Green tick symbol
        else:
            return mark_safe('<span style="color:red">&#10008;</span>')  # Red cross symbol

    list_display = ('employee', 'display_present', 'date', 'location',)  # Remove 'location' from list_display

    display_present.short_description = 'Present'

admin.site.register(Attendance, AttendanceAdmin)
