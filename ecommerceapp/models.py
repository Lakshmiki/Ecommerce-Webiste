from django.db import models


# Create your models here.
class userregister(models.Model):
    fullname=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    phone=models.IntegerField()
    gender=models.CharField(max_length=10)
    propic=models.ImageField(upload_to='image/')
    password=models.CharField(max_length=10)
    def __str__(self):
        return self.fullname
class sellerproductupload(models.Model):
    productname=models.CharField(max_length=30)
    productprice=models.IntegerField()
    productimage=models.ImageField(upload_to='image/')
    productavailsize=models.CharField(max_length=30)
    productdescription=models.CharField(max_length=300)
    productcategory=models.CharField(max_length=30)
    def __str__(self):
        return self.productname
class CartItem(models.Model):
    userid=models.IntegerField()
    item=models.ForeignKey(sellerproductupload,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    selected_size=models.CharField(max_length=20)
    def __str__(self):
        return self.item
class WishList(models.Model):
    userid=models.IntegerField()
    item=models.ForeignKey(sellerproductupload,on_delete=models.CASCADE)
    def __str__(self):
        return self.item
class Address_details(models.Model):
    userdetails=models.ForeignKey(userregister,on_delete=models.CASCADE)
    address_line1=models.CharField(max_length=200)
    address_line2=models.CharField(max_length=200)
    pincode=models.IntegerField()
    city=models.CharField(max_length=20)
    state=models.CharField(max_length=20)
    contact_name=models.CharField(max_length=200)
    contact_number=models.IntegerField()
    def __str__(self):
        return self.contact_name
class Order(models.Model):
    userdetails=models.ForeignKey(userregister,on_delete=models.CASCADE)
    address=models.ForeignKey(Address_details,on_delete=models.CASCADE)
    ordered_date=models.DateTimeField(auto_now_add=True)
class OrderItem(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    order_pic=models.ImageField()
    pro_name=models.CharField(max_length=20)
    quantity=models.IntegerField()
    price=models.IntegerField()
    order_status=models.BooleanField(default=1)











