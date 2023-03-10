from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import RegisterForm


def register(request):
	if request.method == "POST":
		form = RegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Bem-vindo(a), {username}. Sua conta foi criada')
			return redirect('login')
	else:
		form = RegisterForm()
	return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
	return render(request, 'users/profile.html')
