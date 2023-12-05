from django.shortcuts import render
import requests
from django.http import JsonResponse

TELEGRAM_URL = "https://api.telegram.org/bot"
TOKEN = '6840199031:AAFoshpO0dTv2l1rsM9hBLjqL98iL-YNLXI'


def send_bot_info(request):
    if request.method == 'POST' and request.is_ajax():
        name = request.POST.get('name', None)
        phone = request.POST.get('phone', None)
        message = f'Имя: {name} \n Телефон: {phone}'
        data = {
            "chat_id": 6746800266,
            "text": message,
        }
        response = requests.get(
            f"{TELEGRAM_URL}{TOKEN}/sendMessage", data=data
        )
        return JsonResponse({'status': True})
    else:
        return JsonResponse({'status': False})

# Create your views here.
