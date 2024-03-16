from django.db import models
from datetime import date

class Attendance(models.Model):
    employee = models.CharField(max_length=100)
    date = models.DateField(default=date.today)
    present = models.BooleanField(default=False)
    location = models.CharField(max_length=100, blank=True, null=True)

    def get_present_display(self):
        return "Present" if self.present else "Absent"
    get_present_display.short_description = 'Present'
