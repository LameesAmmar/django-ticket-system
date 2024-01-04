from django.shortcuts import render , redirect
from django.contrib import messages
from django.contrib.auth import authenticate , login,logout ,get_user_model
from .form import RegisterCustomerForm
from .models import User
from django.conf.urls.static import static



User= get_user_model()

# Create your views here.
def register_customer(request):
    if request.method == 'POST':
        form = RegisterCustomerForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.is_customer = True 
            var.save()
            messages.info(request,'your account has been successfully registered. Please login ')
            return redirect('login')
        else:
            messages.warning(request,'somting went wrong.Please check form inputs')
            return redirect('register_customer')
    else:
        form = RegisterCustomerForm() 
        context = {'form':form}  
        return render(request,'users/register_customer.html',context) 

#login a user
def login_user(request):
    if request.method =='POST' :
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None and user.is_active:
            login(request,user)
            messages.info(request,'Login successfull .Please enjoy')
            return redirect('dashboard')
        else:
            messages.warning(request, 'something went wrong.please check form input')
            return redirect('login')
    else:
        return render(request, 'users/login.html')
    

#logout user

def logout_user(request)  :
    logout(request)
    messages.info(request,'Your session has ended')
    return redirect('login')


