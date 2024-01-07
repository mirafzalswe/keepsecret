from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect

from django.contrib.auth.views import LoginView, LogoutView

from django.views import View
from django.views.generic import CreateView, TemplateView
from .forms import RegistrationForm, ProfileUpdateForm
from .models import Profile
class LoginUser(LoginView):
    template_name = 'user/login.html'


def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login-page')
    else:
        form = RegistrationForm()

    return render(request, 'user/singup.html', {'form': form})



class ProfileUser(LoginRequiredMixin, TemplateView):
    login_url = '/login/'
    template_name = 'user/profile.html'



class EditProfileView(LoginRequiredMixin, View):
    login_url = '/login/'
    def get(self, request):
        customer = Profile.objects.get(user=request.user)
        form = ProfileUpdateForm(instance=customer)
        return render(request, 'user/update-profile.html', {'form': form})

    def post(self, request):
        profile = Profile.objects.get(user=request.user)
        form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            print("Profile Updated Successfully")
            return redirect('profile-page')
        else:
            print(form.errors)
        return render(request, 'user/update-profile.html', {'form': form})
