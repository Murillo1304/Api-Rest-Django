from django.shortcuts import render
import base64
import json
import requests
from Keys.keys import keys
# Create your views here.
def home(request):
    context = {
    }
    return render(request,'home.html', context)

def formToken(request):
    mode = request.POST.get('mode')

    username = keys["username"]
    password = keys["password"]
    publickey = keys['publickey']

    url = 'https://api.micuentaweb.pe/api-payment/V4/Charge/CreatePayment'
    auth = 'Basic ' + base64.b64encode(f"{username}:{password}".encode('utf-8')).decode('utf-8')

    data = {
        "amount": 180,
        "currency": "PEN",
        "orderId": "myOrderId-999999",
        "customer": {
            "email": "sample@example.com"
        }
    }

    headers = {
        'Content-Type': 'application/json',
        'Authorization': auth,
    }

    response = requests.post(url, json=data, headers=headers)
    response_data = response.json()

    if response_data['status'] == 'SUCCESS':
        token = response_data['answer']['formToken']

        return render(request, 'Demo/formtoken.html', {'mode': mode, 'token': token, 'publickey': publickey})
    else:
        print(response.status_code)