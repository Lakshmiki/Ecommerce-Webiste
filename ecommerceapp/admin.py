from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(userregister)
admin.site.register(sellerproductupload)
admin.site.register(CartItem)
admin.site.register(WishList)
admin.site.register(Address_details)
admin.site.register(Order)
admin.site.register(OrderItem)


