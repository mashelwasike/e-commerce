from django.http import JsonResponse
from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def index(request):
    wishlist = Wishlist.objects.filter(user=request.user)
    context ={'wishlist':wishlist}
    return render(request,'store/products/wishlist.html',context)

def addtowishlist(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            prod_id = int(request.POST.get('product_id'))
            product_check =  Product.objects.get(id=prod_id)
            if(product_check):
                if(Wishlist.objects.filter(user = request.user,product_id =prod_id)):
                    return JsonResponse({'status':'Product already in wishlist'})
                else:
                    Wishlist.objects.create(user = request.user,product_id =prod_id)
                    return JsonResponse({'status':'Product added succesfully'})
            else:
                return JsonResponse({'status':'Product added to wishlist'})
            
        return JsonResponse({'status':'Login to continue'})
    return redirect('/')

def deleteitem(request):
    if request.method == "POST":
        prod_id = int(request.POST.get('product_id'))
        if(Wishlist.objects.filter(user=request.user,product_id = prod_id)):
            wishlistitem = Wishlist.objects.get(product_id = prod_id, user=request.user)
            wishlistitem.delete()
            return JsonResponse({'status':'Item deleted'})
        else:
            return JsonResponse({'status':'items not found in the wishlist'})
    return redirect('/')