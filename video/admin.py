from django.contrib import admin
from .models import Category, Project, ContactMessage
admin.site.register(Category)
admin.site.register(Project)
admin.site.register(ContactMessage)