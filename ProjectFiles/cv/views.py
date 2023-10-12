from .models import Project
from django.shortcuts import render
from django.views.generic import DetailView, ListView, TemplateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse

# Create your views here.


@login_required()
def home(request):
	return render(request, 'cv/home.html')


@login_required()
def test(request):
	return render(request, 'cv/test.html')


class DashboardView(LoginRequiredMixin, TemplateView):
	template_name = 'accounts/dashboard-base.html'


class ProjectsView(LoginRequiredMixin, ListView):
	model = Project
	template_name = 'accounts/dashboard-projects.html'


class ProjectDetailView(LoginRequiredMixin, DetailView):
	model = Project
	template_name = 'accounts/dashboard-project-detail.html'


class ProjectCreateView(LoginRequiredMixin, CreateView):
	model = Project
	template_name = 'accounts/dashboard-project-add.html'
	fields = ['start_date']

	def form_valid(self, form):
		user = self.request.user
		form.instance.leader = user
		return super(ProjectCreateView, self).form_valid(form)
	
	def get_success_url(self):
		return reverse('project-detail', kwargs={'pk': self.object.pk})


class ProfileView(LoginRequiredMixin, TemplateView):
	template_name = 'cv/profile_template.html'
