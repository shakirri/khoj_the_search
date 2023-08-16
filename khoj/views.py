from django.shortcuts import render
from django.http import HttpResponse
import requests
from django.shortcuts import redirect
from .models import Users,UserData
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required(login_url='login')
def check(request):
    if request.user.is_authenticated:
        user=request.user
    else:
        return redirect('login')
    try:
        val= request.POST['values']
        n= request.POST['num']
        n=int(n)
        number_strings = val.split(',')
        number_list = [int(num.strip()) for num in number_strings]
        num_list = sorted(number_list, reverse=True)
        int_list_string = ','.join(map(str, num_list))
        user_data = UserData.objects.create(user=user, input_values=int_list_string)
        if n in num_list:
            messages.success(request, f'True')
        else:
            messages.success(request, f'False')
    except UnboundLocalError:
        messages.error(request, f'Input Correctly')
    except ValueError:
        messages.error(request, f'Input Correctly')
     
    return redirect('home')
