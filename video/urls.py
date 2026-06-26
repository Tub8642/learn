from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.project_list, name='home'),
    path('contact/', views.contact_view, name ='contact'),
]