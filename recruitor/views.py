from django.shortcuts import redirect
from django.shortcuts import render
from django.views.generic import TemplateView,CreateView,ListView,FormView,DeleteView,UpdateView,DetailView
from django.urls import reverse_lazy
from .models import Company
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class CreateCompany(CreateView,LoginRequiredMixin):
    model=Company
    fields=['phone','email','looking_for']
    success_url=reverse_lazy('recruitor:list1')
    def form_valid(self,form):
        self.object=form.save(commit=False)
        self.object.user=self.request.user
        self.object.save()
        return super().form_valid(form)


class ListCompany(ListView):
    model=Company
    context_object_name='tasks1'

class DetailCompany(DetailView):
    model=Company

class DeleteCompany(DeleteView,LoginRequiredMixin):
    model=Company
    success_url=reverse_lazy('recruitor:list1')

class UpdateCompany(LoginRequiredMixin,UpdateView):
    model=Company
    fields=['phone','email','looking_for']
    success_url=reverse_lazy('recruitor:list1')
