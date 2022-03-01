from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView,TemplateView
from django.contrib.auth.views import LoginView,LogoutView
from . import forms
# Create your views here.


class SignUp(CreateView):
    form_class=forms.UserSignUpForm
    success_url=reverse_lazy('login')
    template_name='accounts/SignUp.html'

class CSignUp(CreateView):
    form_class=forms.UserSignUpForm
    success_url=reverse_lazy('login1')
    template_name='accounts/SignUp.html'

class CustomLoginView(LoginView):
    template_name='accounts/login.html'
    fields='__all__'

    redirect_authenticated_user=True   ##so that if the user is already logged in its is redirected##

    def get_success_url(self):
        return reverse_lazy('jobs_app:list')


class CompanyLoginView(LoginView):
    template_name='accounts/login.html'
    fields='__all__'

    redirect_authenticated_user=True   ##so that if the user is already logged in its is redirected##

    def get_success_url(self):
        return reverse_lazy('recruitor:list1')



class CustomLogoutView(LogoutView):
    template_name='accounts/thanks.html'

class CLogoutView(LogoutView):
    template_name='accounts/thanks1.html'
