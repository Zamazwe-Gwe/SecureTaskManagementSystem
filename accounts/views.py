from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from auditlog.models import AuditLog
from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
    return render(request, 'accounts/profile.html')

def register(request):
    form = UserCreationForm(request.POST or None)

    if form.is_valid():
        user = form.save()
        login(request, user)

        AuditLog.objects.create(
            user=user,
            action="Registered and logged in"
        )

        return redirect('task_list')

    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if form.is_valid():
        user = form.get_user()
        login(request, user)

        AuditLog.objects.create(
            user=user,
            action="Logged in"
        )

        return redirect('task_list')

    return render(request, 'accounts/login.html', {'form': form})


@login_required
def logout_view(request):
    AuditLog.objects.create(
        user=request.user,
        action="Logged out"
    )

    logout(request)
    return redirect('login')