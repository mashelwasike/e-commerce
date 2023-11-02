from django.http import JsonResponse
from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages

def checkout_view(request):
    rawcart = Cart.objects.filter(user=request.user)
    for item in rawcart :
        if item.product_qty > item.product.quantity:
            deleteitem=Cart.objects.get(id=item.id)
            deleteitem.delete()

    cartitems = Cart.objects.filter(user=request.user)
    total_price=0
    for item in cartitems:
        total_price = total_price + item.product.price * item.product_qty
    
    userprofile = Profile.objects.filter(user=request.user).first()

    context ={'cartitems':cartitems,'total_price':total_price,'userprofile':userprofile}
    return render(request,'store/products/checkout.html',context)

@login_required(login_url='login')
def placeorder(request):
    if request.method == 'POST':

        currentuser = User.objects.filter(id = request.user.id).first()
        if not currentuser.first_name:
            currentuser.first_name = request.POST.get('fname')
            currentuser.last_name = request.POST.get('lname')
            currentuser.save()

        if not Profile.objects.filter(user=request.user):
            userprofile = Profile()
            userprofile.user = request.user
            userprofile.email = request.POST.get('email')
            userprofile.phoneno = request.POST.get('phoneno')
            userprofile.address = request.POST.get('address')
            userprofile.city = request.POST.get('city')
            userprofile.county = request.POST.get('county')
            userprofile.street = request.POST.get('street')
            userprofile.save()

        neworder = Order()
        neworder.user = request.user
        neworder.fname = request.POST.get('fname')
        neworder.lname = request.POST.get('lname')
        neworder.email = request.POST.get('email')
        neworder.phoneno = request.POST.get('phoneno')
        neworder.address = request.POST.get('address')
        neworder.city = request.POST.get('city')
        neworder.county = request.POST.get('county')
        neworder.street = request.POST.get('street')

        cart = Cart.objects.filter(user=request.user)
        cart_item_total = 0
        if (cart):
            for item in cart:
                cart_item_total=cart_item_total + item.product.price * item.product_qty
        
        neworder.total_price = cart_item_total
        neworder.save()

        neworderitems = Cart.objects.filter(user = request.user)
        for item in neworderitems:
            OrderItem.objects.create(
                order = neworder,
                product = item.product,
                price= item.product.price,
                quantity = item.product_qty
            )
            orderproduct = Product.objects.filter(id=item.product_id).first()
            orderproduct.quantity = orderproduct.quantity - item.product_qty
            orderproduct.save()

        Cart.objects.filter(user = request.user).delete()
        messages.success(request,"Your order has been placed succesfully")

    return redirect('/')