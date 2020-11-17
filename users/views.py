from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f"Account Created successfully! You can now login")
            return redirect('/')
    form = UserRegisterForm()
    context= {
        'form': form
    }
    return render(request, 'users/register.html', context)
