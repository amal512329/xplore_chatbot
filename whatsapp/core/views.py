from django.shortcuts import render,redirect
from django.http import HttpResponse
from .secret_key import API_KEY
import openai
from .chat_gpt import get_chat_response
import json
# Create your views here.
openai.api_key = API_KEY


def home(request):
    return render(request,'core/home.html')


    
def index(request):
    
    return render(request, "core/index.html")

def chat_gpt(request):
    
    response = get_chat_response(request.GET.get('prompt'))
    # print(response)

    return HttpResponse(json.dumps(response), content_type='application/json')


def WhatsappData(Ph,Message):
    import time
    import webbrowser as web
    import pyautogui as pg
    Phone = '91'+ Ph
    web.open('https://web.whatsapp.com/send?phone=' +Phone+'&text='+Message)


def SendData(request):
    if request.method == 'POST':
        Ph = request.POST['Phone']
        Message = request.POST['Message']
        WhatsappData(Ph,Message)
        msg = 'Message has successfully sent..'
        return render(request,'core/home.html',{'msg':msg})
    else:
        return HttpResponse('404 Error !')