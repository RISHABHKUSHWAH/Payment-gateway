# from django.conf import settings
# import requests
# from .views import calculateCharges
# from django.contrib.auth.models import User
# from .models import Order
# from django.shortcuts import redirect
# from instamojo_wrapper import Instamojo
# api = Instamojo(api_key=settings.API_KEY,
# auth_token= settings.AUTH_TOKEN,endpoint='https://test.instamojo.com/api/1.1/')
# # API_ENDPOINT = 'https://test.instamojo.com/@testpay6397/'

# def order(request):
#         obj = calculateCharges(request.GET.get('type'))
#         amount= obj['sum']
#         purpose = request.GET.get('type')
#         user_id = request.user.id
#         buyer_name = User.objects.get(id=user_id)
#         # email = User.objects.get(email = request.user.Emailaddress)
#         phone = '6397969483'
        
#         response = api.payment_request_create(
#         amount=amount,
#         purpose=purpose,
#         buyer_name = buyer_name,
#         send_email=True,
#         email= 'kushwah@yopmail.com',
#         phone = phone,
#         redirect_url="http://127.0.0.1:8000/card/orderComfirm/") 
        
#         orderObj = Order(
#             user = User.objects.get(id= request.user.id), 
#             productName = response['payment_request']['purpose'],
#             purpose = response['payment_request']['purpose'],
#             amount = response['payment_request']['amount'],
#             status = response['payment_request']['status'],
#             payment_request_id = response['payment_request']['id'],
#             created_at = response['payment_request']['created_at'],
#             modified_at = response['payment_request']['modified_at'],
#             webhook_url = response['payment_request']['modified_at']
#         )
#         orderObj.save()
#         responseStr =response['payment_request']['longurl']
#         print(responseStr)
#         return redirect('https://test.instamojo.com/@testpay6397/b2ab5994d6c048b9b8e4ff2b57566c20')