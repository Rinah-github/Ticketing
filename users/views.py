from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterCustomerForm

# registering a customer

def register_customer(request):
    if request.method == 'POST':
        form = RegisterCustomerForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.is_customer = True
            var.save()
            messages.info(request, 'Your account registered successfully')
            return redirect('login')
        else:
            messages.warning(request, 'Something went wrong. Please check form inputs')
            return redirect('register-customer')        
    else:
        form = RegisterCustomerForm()
        context ={'forms':form}
        return render(request, 'user/register_customer.html', context)
    


#login user
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username='username', password='password')
        if user is not None and user.is_active:
            login(request, user)
            messages.info(request, 'Login successful. Pease enjoy ypur session')
            return redirect('dashboard')
        else:
            messages.warning(request, 'Something went worng. Check form inputs')
            return redirect('login')
    else:
        return render(request, 'user/login.html')
    

#logout
def user_logout(request):
    user_logout(request)
    messages.info(request, 'Your session has ended. Please log in to continue')
    return redirect('login')

