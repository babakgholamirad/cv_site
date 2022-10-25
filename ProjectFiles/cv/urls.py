from django.urls import path

from .views import (
    DashboardView,
    ProjectsView,
    ProjectDetailView,
    ProjectCreateView,
    test, ProfileView)

urlpatterns = [
    path('', DashboardView.as_view(), name='home'),
    path('test/', test, name='test'),
    path('dashboard/projects/add',
         ProjectCreateView.as_view(), name='project-detail-add'),
    path('dashboard/projects/<int:pk>',
         ProjectDetailView.as_view(), name='project-detail'),
    path('dashboard/projects/', ProjectsView.as_view(), name='projects'),
    path('dashboard/profile/', ProfileView.as_view(), name='profile'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
]
