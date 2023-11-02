from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    slug = models.CharField(max_length=150,null=False,blank=False)
    name = models.CharField(max_length=150,null=False,blank=False)
    image = models.ImageField(null=False,blank=False)
    description = models.TextField(max_length=700,null=False,blank=False)
    status = models.BooleanField(default=False,help_text="0=default,1=Trending")
    trending = models.BooleanField(default=False,help_text="0=default,1=Trending")
    meta_title = models.CharField(max_length=150,null=False,blank=False)
    meta_keywords = models.CharField(max_length=150,null=False,blank=False)
    meta_description = models.CharField(max_length=150,null=False,blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url=''
        return url

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.CharField(max_length=150,null=False,blank=False)
    name = models.CharField(max_length=150,null=False,blank=False)
    image = models.ImageField(null=False,blank=False)
    small_description = models.TextField(max_length=500,null=False,blank=False)
    quantity = models.IntegerField(null=True,blank=True)
    description = models.TextField(max_length=2000,null=False,blank=False)
    price = models.FloatField(null=False,blank=False)
    status = models.BooleanField(default=False,help_text="0=default, 1=Hidden")
    trending = models.BooleanField(default=False,help_text="0=default, 1=Trending")
    tag = models.CharField(max_length=150,null=False,blank=False)
    meta_title = models.CharField(max_length=150,null=False,blank=False)
    meta_keywords = models.CharField(max_length=150,null=False,blank=False)
    meta_description = models.CharField(max_length=150,null=False,blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.ForeignKey(User,on_delete= models.CASCADE)
    product =models.ForeignKey(Product,on_delete= models.CASCADE)
    product_qty=models.IntegerField(null=False,blank=False)
    created = models.DateTimeField(auto_now_add=True)
    
class Wishlist(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    fname = models.CharField(max_length=150,null=False)
    lname= models.CharField(max_length=150,null=False)
    email=models.EmailField(max_length=150,null=False)
    phoneno=models.CharField(max_length=150,null=False)
    address=models.CharField(max_length=150,null=False)
    city=models.CharField(max_length=150,null=False)
    county=models.CharField(max_length=150,null=False)
    street =models.CharField(max_length=150,null=False)
    total_price = models.FloatField(null=False)
    payment_id= models.CharField(max_length=250,null=False)
    orderstatus = (
        ('Pending','Pending'),
        ('Out For Shipping','Out For shipping'),
        ('Completed','Completed')
    )
    status = models.CharField(max_length=150,choices=orderstatus,default='Pending')
    message = models.TextField(null=True)
    tracking_no = models.CharField(max_length=150,null=True)

    def __str__(self):
        return '{}-{}'.format(self.id, self.tracking_no)
    


# class Order(models.Model):
class OrderItem(models.Model):
    order= models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    price= models.FloatField(null=False)
    quantity=models.IntegerField(null=False)

    def __str__(self):
        return '{}-{}'.format(self.order.id, self.order.tracking_no)
    
    @property
    def item_total_price(self):
        total = self.price * self.quantity
        return total
    
class Profile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    fname = models.CharField(max_length=150,null=False)
    lname= models.CharField(max_length=150,null=False)
    email=models.EmailField(max_length=150,null=False)
    phoneno=models.CharField(max_length=150,null=False)
    address=models.CharField(max_length=150,null=False)
    city=models.CharField(max_length=150,null=False)
    county=models.CharField(max_length=150,null=False)
    street =models.CharField(max_length=150,null=False)
    created =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username