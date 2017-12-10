from django.shortcuts import render, redirect

from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required


@login_required(login_url='/home/')
def logout(request):
    auth_logout(request)
    return redirect('/home/')


def redirect_to_home(request):
    return redirect('/home/')


def home(request):
    context = {'active_tab': 'home'}
    login_error_msg = request.session.pop('login_error_msg', None)
    if login_error_msg:
        context['login_error_msg'] = login_error_msg

    return render(request, 'apps/core/home.html', context=context)


def about(request):
    context = {'active_tab': 'about'}
    return render(request, 'apps/core/about.html', context=context)


def projects(request):
    context = {'active_tab': 'projects'}
    return render(request, 'apps/core/projects.html', context=context)

def calendar(request):
    context = {'active_tab': 'calendar'}
    return render(request, 'apps/core/calendar.html', context=context)
	
def recruitment(request):
    context = {'active_tab': 'recruitment'}
    return render(request, 'apps/core/recruitment.html', context=context)
