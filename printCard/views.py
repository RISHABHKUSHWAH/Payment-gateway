from django.shortcuts import render,redirect
from .models import Id_card,Adhar_card,Pan_card
from orders.models import Products
from django.contrib.auth.models import User
# Create your views here.

def id_card(request):
    if request.method == "POST":
        user_id = request.user.id
        user = User.objects.get(id=user_id)
        name = request.POST['name']
        mob = request.POST['mob']
        address = request.POST['address']
        file = request.FILES['file']
        save_id = Id_card(user=user,name = name ,mobile = mob, address = address, file = file)
        save_id.save()
        return redirect('/card/amountOfOrder?type=idcard')
    product = Products.objects.filter(productName='idcard') 
    firstrow = product.first()
    return render(request,'idcard.html',{'amount':firstrow.amount})

def adharcard(request):
    if request.method == "POST":
        user_id = request.user.id
        user = User.objects.get(id=user_id)
        name = request.POST['name']
        mob = request.POST['mob']
        address = request.POST['address']
        password = request.POST['password']
        file = request.FILES['file']
        save_id = Adhar_card(user = user,name =name ,mobile = mob, address = address,password = password, file = file)
        save_id.save()
        return redirect('/card/amountOfOrder?type=adharcard')
    product = Products.objects.filter(productName='adharcard') 
    firstrow = product.first()    
    return render(request,'adharcard.html',{'amount':firstrow.amount})

def pancard(request):
    if request.method == "POST":
        user_id = request.user.id
        user = User.objects.get(id=user_id)
        name = request.POST['name']
        mob = request.POST['mob']
        address = request.POST['address']
        file = request.FILES['file']
        save_id = Pan_card(user = user ,name=name ,mobile = mob, address = address, file = file)
        save_id.save()
        return redirect('/card/amountOfOrder?type=pancard')
    product = Products.objects.filter(productName='pancard') 
    firstrow = product.first()    
    return render(request,'pancard.html',{'amount':firstrow.amount})    
    
