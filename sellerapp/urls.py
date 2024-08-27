from django.urls import path
from . import views

urlpatterns=[
    path('register/',views.register_seller,name='register'),
    path('login/',views.login_view,name='login'),
    path('seller_index/',views.seller_index,name='seller_index'),
    # path('seller_profile/',views.seller_profile,name='seller_profile'),
    path('uploadsellerproduct/',views.uploadsellerproduct,name='uploadsellerproduct'),
    path('seller_profile/',views.view_seller_upload_product,name='seller_profile'),
    # path('seller_profile/<int:cartid>',views.delete_seller_product,name='seller_profile')
    # path('delete_seller_product/<int:cartid>',delete)

]