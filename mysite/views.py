from multiprocessing import context
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView

from .models import *
from .forms import *


def index(request):
    main_doctor = MainDoctor.objects.all()
    context = {'main_doctor': main_doctor}
    return render(request, 'index.html', context=context)


def hospital(request):
    hospital_info = Hospital.objects.all()
    context = {'hospital_info': hospital_info}
    return render(request, 'hospital.html', context=context)


def main_doctor(request, pk):   
    main_doctor = MainDoctor.objects.get(pk=pk)
    context = {'main_doctor': main_doctor}
    return render(request, 'main_doctor.html', context=context)


def patient(request):
    patients = Patient.objects.all()
    context = {'patients': patients}
    return render(request, 'patient.html', context=context)


def treat_doctor(request):
    treat_doctor = TreatDoctor.objects.all().select_related().distinct()
    context = {'treat_doctor': treat_doctor}
    return render(request, 'treat_doctor.html', context=context)
    

class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'register.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('index')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'login.html'

    def get_success_url(self):
        return reverse_lazy('index')


def logout_user(request):
    logout(request)
    return redirect('index')