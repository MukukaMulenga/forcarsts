from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
import requests
from  .forms import City
# Create your views here.



def get_default_weather(request):
    name = 'lusaka'
    response = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+name+"&appid=8a7580b58ce09a39f9d8e87faf6c72eb")
    api_data = response.json()
    form = City()
    return render(request,'main.html',{'form':form,'info':api_data})


def get_wether(request):
    if request.method == "GET":
       form = City(request.GET)
       if form.is_valid():
           name = form.cleaned_data['name']
           response = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+name+"&appid=8a7580b58ce09a39f9d8e87faf6c72eb")
           api_data = response.json()
           form = City()
           return render(request,'main.html',{'form':form,'info':api_data})          
    else:
        form = City()
    
    





# def get_wether(request):
#         response = requests.get('https://api.openweathermap.org/data/2.5/weather?q=lusaka&appid=8a7580b58ce09a39f9d8e87faf6c72eb')
#         api_data = response.json()
#         # return render(request,'main.html',{'api_data':api_data})
#         return JsonResponse(api_data,safe=False)
       
        
   