from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .forms import RegisterForm


class UserRegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')


class UserLoginView(LoginView):
    template_name = 'login.html'


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('login')


@login_required
def dashboard(request):
    return render(request, 'dashboard.html')
