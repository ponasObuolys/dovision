from django.contrib.auth.forms import UserCreationForm, PasswordResetForm, SetPasswordForm
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


def Reset_Password_View(request):
    form = PasswordResetForm
    context = {'form': form}
    return render(request, 'registration/reset_password.html', context)


def Reset_Password_Done_View(request):
    return render(request, 'registration/reset_password_done.html')