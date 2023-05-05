from django.shortcuts import render,redirect
from .models import Products
from django.conf import settings
from .models import Order
from datetime import datetime
from django.contrib.auth.models import User
from instamojo_wrapper import Instamojo
api = Instamojo(api_key=settings.API_KEY,
auth_token= settings.AUTH_TOKEN,endpoint='https://test.instamojo.com/api/1.1/')

def amountOfOrder(request):
    obj = calculateCharges(request.GET.get('type'))
    print(request.GET.get('type'))
    if request.method == 'POST':
        obj = calculateCharges(request.GET.get('type'))
        amount= obj['sum']
        purpose = request.GET.get('type')
        user_id = request.user.id
        buyer_name = User.objects.get(id=user_id)
        phone = '6397969483'
        
        response = api.payment_request_create(
        amount=amount,
        purpose=purpose,
        buyer_name = buyer_name.username,
        send_email=True,
        email= buyer_name.email,
        phone = phone,
        redirect_url="http://127.0.0.1:8000/card/orderComfirm/") 

        orderObj = Order(
            user = User.objects.get(id= request.user.id), 
            productName = response['payment_request']['purpose'],
            purpose = response['payment_request']['purpose'],
            amount = response['payment_request']['amount'],
            status = response['payment_request']['status'],
            payment_request_id = response['payment_request']['id'],
            created_at = response['payment_request']['created_at'],
            modified_at = response['payment_request']['modified_at'],
            webhook_url = response['payment_request']['webhook']
        )
        orderObj.save()
        responseStr =response['payment_request']['longurl']
        return redirect(responseStr)
    formAction ='?type='+request.GET.get('type')
    return render(request,'order.html',{'price':obj['price'],'sum':obj['sum'],'formAction':formAction})

def orderConfirm(request):
    currentTime = datetime.now()
    status = request.GET.get('payment_status')
    order = Order.objects.get(payment_request_id= request.GET.get('payment_request_id'))
    order.status = status
    order.modified_at = currentTime.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
    order.save()
    return render(request,'orderSucc.html')

def calculateCharges(type):
    product = Products.objects.filter(productName=type) 
    firstrow = product.first()
    sum = firstrow.amount + firstrow.deliveryCharge
    prices = {'price':firstrow,'sum':sum}
    return prices