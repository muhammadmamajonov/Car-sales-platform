from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.admin.forms import AdminAuthenticationForm



def docs_login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('/docs/')
        else:
            return redirect('/docs/login')

    return render(request, 'admin/login.html', context={'form': AdminAuthenticationForm})
