from .models import Project, Member
from django.shortcuts import render
from django.views.generic import DetailView, ListView, TemplateView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib import messages

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
	fields = ['title',
			  'client',
			  'description',
			  'status',
			  'start_date']

	def form_valid(self, form):
		user = self.request.user
		form.instance.leader = user
		messages.success(self.request, "The project was created successfully.")
		return super(ProjectCreateView, self).form_valid(form)

	def get_success_url(self):
		return reverse('project-detail', kwargs={'pk': self.object.pk})

	def get_context_data(self, *args, **kwargs):
		context = super(CreateView, self).get_context_data(*args, **kwargs)
		context['all_members'] = Member.objects.all()
		return context


class ProjectDeleteView(LoginRequiredMixin, DeleteView):
	model = Project
	template_name = "accounts/dashboard-project-delete.html"

	def form_valid(self, form):
		messages.success(self.request, "The project was deleted successfully.")
		return super(ProjectDeleteView, self).form_valid(form)

	def get_success_url(self):
		return reverse('projects')


class ProfileView(LoginRequiredMixin, TemplateView):
	template_name = 'cv/profile_template.html'
