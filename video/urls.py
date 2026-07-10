from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet

router = DefaultRouter()
router.register(r'projects', ProjectViewSet)

urlpatterns = [
    path('home/', views.project_list, name='home'),
    path('contact/', views.contact_view, name ='contact'),
    path('api/', include(router.urls)),
]