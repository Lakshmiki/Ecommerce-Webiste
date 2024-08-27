
from django.urls import path
from.views import *
urlpatterns=[path('index/',index),
             path('Userregistration/',Userregistration),
             path('Userlogin/',Userlogin),
             path('userprofile/',userprofile),
             path('viewdetails/',viewdetails),
             path('updateuserdetails/',updateuserdetails),
             # path('uploadsellerproduct/',uploadsellerproduct),
             path('addtocart/<int:itemid>',addtocart),
             path('viewproducts/',viewproducts),
             path('cartdisplay/',cartdisplay),
             path('incdec/<int:cartid>',incdec),
             path('deletecart/<int:cartid>',deletecart),
             path('wishlist/<int:itemid>',wishlist),
             path('wishlistdisplay/',wishlistdisplay),
             path('delete_from_wishlist/',delete_from_wishlist),
             path('add_address/',add_address),
             path('delivaryaddress/',delivaryaddress),
             path('summarypage/',summarypage),
             path('create_order/',create_order),
             path('orderview/',orderview),
             path('order_confirmation_email/',create_order),
             path('order_cancel/<int:id>',order_cancel),
             path('samplecard/',samplecard),
             path('change_password_user/',change_password_user),
             path('logout/',logout)


             ]

