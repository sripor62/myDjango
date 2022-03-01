from django.shortcuts import redirect
from django.shortcuts import render
from django.views.generic import TemplateView,CreateView,ListView,FormView,DeleteView,UpdateView,DetailView
from .models import Application
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class HomePage(TemplateView):
    template_name='jobs_app/index.html'

class ListProfile(ListView):
    model=Application
    context_object_name='tasks'
    ##so that now each user can see only his tasks

class CreateProfile(CreateView,LoginRequiredMixin):
    model=Application
    fields=['phone','email','gender','profile_pic','Education_last','skills','achievements']
    success_url=reverse_lazy('jobs_app:list')

    def form_valid(self,form):
        self.object=form.save(commit=False)
        self.object.user=self.request.user
        self.object.save()
        return super().form_valid(form)

class DeleteProfile(DeleteView,LoginRequiredMixin):
    model=Application
    success_url=reverse_lazy('jobs_app:list')

class UpdateProfile(LoginRequiredMixin,UpdateView):
    model=Application
    fields=['phone','email','gender','profile_pic','Education_last','skills','achievements']
    success_url=reverse_lazy('jobs_app:list')

class DetailProfile(DetailView):
    model=Application
