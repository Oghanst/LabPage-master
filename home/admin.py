from django.contrib import admin

from .models import Student, Professor, Project, Paper, News

admin.site.register(Student)
admin.site.register(Professor)
admin.site.register(Project)
admin.site.register(Paper)
admin.site.register(News)
