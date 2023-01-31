from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


def login_views(request):
    if not request.user.is_anonymous:
        return redirect('blog:index')
    form = AuthenticationForm(request)
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            next_page = request.GET.get('next')
            if next_page:
                return redirect(next_page)
            return redirect('blog:index')
    context = {
        'form': form
    }
    return render(request, 'account/login.html', context)


def logout_views(request):
    if not request.user.is_authenticated:
        return redirect('account:login')
    if request.method == "POST":
        logout(request)
        return redirect('account:login')
    return render(request, 'account/logout.html')


def register_views(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('account:login')
    context = {
        'form': form
    }
    return render(request, 'account/register.html', context)

