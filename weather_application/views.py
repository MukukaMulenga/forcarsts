from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
import requests
# Create your views here.


def show_data(request,information):
        info = information
        return render(request,'main.html',{'info':info})

def get_wether(request,location):
        name = location
        response = requests.get('https://api.weatherapi.com/v1/current.json?key=35bc48d5069f456c95792555232012&q=name&lang=english')
        api_data = response.json()
        show_data(api_data)
        return JsonResponse(api_data)
       
        
   