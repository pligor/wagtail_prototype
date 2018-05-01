from django.contrib import admin

# Register your models here.
from .models import UserProfile, Project, Task, Supervisor, Developer
admin.site.register(UserProfile)
admin.site.register(Project)
admin.site.register(Task)
admin.site.register(Supervisor)
admin.site.register(Developer)
