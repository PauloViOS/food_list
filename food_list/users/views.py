from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


def register(request):
	if request.method == "POST":
		form = UserCreationForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			messages.success(request, f'Bem-vindo(a), {username}. Sua conta foi criada')
			return redirect('food:index')
	else:
		form = UserCreationForm()
	return render(request, 'users/register.html', {'form': form})
