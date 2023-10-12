from .models import Project
from django.shortcuts import render
from django.views.generic import DetailView, ListView, TemplateView, CreateView
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):

	return render(request, 'cv/home.html')


def test(request):

	return render(request, 'cv/test.html')

@login_required
class DashboardView(TemplateView):
	template_name = 'accounts/dashboard-base.html'

@login_required
class ProjectsView(ListView):
	model = Project
	template_name = 'accounts/dashboard-projects.html'

@login_required
class ProjectDetailView(DetailView):
	model = Project
	template_name = 'accounts/dashboard-project-detail.html'

@login_required
class ProjectCreateView(CreateView):
	model = Project
	template_name = 'accounts/dashboard-project-add.html'
	fields = ['start_date']
	
	def form_valid(self, form):
		user = self.request.user
		form.instance.leader = user
		return super(ProjectCreateView, self).form_valid(form)

@login_required
class ProfileView(TemplateView):
	template_name = 'cv/profile_template.html'
