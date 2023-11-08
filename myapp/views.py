from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.http import JsonResponse

# Create your views here.
def home(request):
    trending_products = Product.objects.filter(trending = 1)
    context = {'trending':trending_products}
    return render(request,'store/index.html',context)

def collection(request):
    category = Category.objects.filter(status = 0)
    context={'category':category}
    return render(request, 'store/collection.html',context)

def collectionview(request,slug):
    if(Category.objects.filter(slug =slug,status = 0)):
        products = Product.objects.filter(category__slug = slug)
        category= Category.objects.filter(slug=slug).first()
        context ={'products':products,'category':category}
        return render(request, 'store/products/products.html',context)
    
    else:
        messages.warning(request,'no such category')
        return redirect('collection')
    
def productview(request, cate_slug, prod_slug):
    if(Category.objects.filter(slug = cate_slug,status=0)):
        if(Product.objects.filter(slug= prod_slug,status=0)):
            products = Product.objects.filter(slug= prod_slug,status=0).first()
            context ={'products':products}
        else:
            messages.error(request,"no such product")
            return redirect('collection')
    else:
        messages.error(request,"No such category")
        return redirect('collection')
    return render(request,'store/products/view.html',context)

def productlist(request):
    products = Product.objects.filter(status = 0).values_list('name',flat=True)
    mylist = list(products)
    return JsonResponse(mylist,safe=False)

def searchproduct(request):
    if request.method == "POST":
        searchItem = request.POST.get('productsearch')
        if searchItem == "":
            return redirect(request.META.get('HTTP_REFERER'))
        else:
            product = Product.objects.filter(name__contains=searchItem).first()

            if product:
                return redirect('collection/'+product.category.slug+'/'+ product.slug)
            else:
                messages.info(request,"product not found")
                return redirect(request.META.get('HTTP_REFERER'))

    return redirect(request.META.get('HTTP_REFERER'))

    
