from django.urls import path

from .views import (
	DashboardView,
	ProjectsView,
	ProjectDeleteView,
	ProjectDetailView,
	ProjectCreateView,
	test, ProfileView)

urlpatterns = [
	path('', DashboardView.as_view(), name='home'),
	path('test/', test, name='test'),
	path('dashboard/projects/', ProjectsView.as_view(), name='projects'),
	path('dashboard/project/add', ProjectCreateView.as_view(), name='project-add'),
	
	path('dashboard/project/<int:pk>',
		ProjectDetailView.as_view(), name='project-detail'),
 
	path('dashboard/project/delete/<int:pk>',
		ProjectDeleteView.as_view(), name='project-delete'),	
	
	path('dashboard/profile/', ProfileView.as_view(), name='profile'),
	path('dashboard/', DashboardView.as_view(), name='dashboard'),
]
