from django.contrib import admin
from .models import Student, Project, ProjectSkills,UserProfile, UserSkills


admin.site.register(Student)
admin.site.register(UserProfile)
admin.site.register(Project)
admin.site.register(ProjectSkills)
admin.site.register(UserSkills)
