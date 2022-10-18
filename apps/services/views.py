from django.shortcuts import render,redirect
from .models import Car,Rent

def service(request):
      print(request.POST.get('where'))
      return render(request, 'services.html')