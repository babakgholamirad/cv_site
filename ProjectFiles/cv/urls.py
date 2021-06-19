from django.urls import path
from .views import (
    DashboardView,
    ProjectsView,
    ProjectDetailView, home, test)
urlpatterns = [
    path('', home, name='home'),
    path('test/', test, name='test'),
    path('dashboard/projects/<int:pk>',
         ProjectDetailView.as_view(), name='project-detail'),
    path('dashboard/projects/', ProjectsView.as_view(), name='projects'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
]
