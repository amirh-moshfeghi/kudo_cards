from django.contrib import admin

from authentication.models import Employee, Department, Team
from .models import Kudo

admin.site.register(Kudo)
admin.site.register(Employee)
admin.site.register(Department)
admin.site.register(Team)
