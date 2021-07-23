from cv.models import Project
from django.shortcuts import render
from django.views.generic import DetailView, ListView, TemplateView, CreateView
# Create your views here.


def home(request):

	return render(request, 'cv/home.html')


def test(request):

	return render(request, 'cv/test.html')


class DashboardView(TemplateView):
	template_name = 'accounts/dashboard-base.html'


class ProjectsView(ListView):
	model = Project
	template_name = 'accounts/dashboard-projects.html'


class ProjectDetailView(DetailView):
	model = Project
	template_name = 'accounts/dashboard-project-detail.html'


class ProjectCreateView(CreateView):
	model = Project
	template_name = 'accounts/dashboard-project-add.html'
	fields = ['start_date']
	
	def form_valid(self, form):
		user = self.request.user
		form.instance.leader = user
		return super(ProjectCreateView, self).form_valid(form)