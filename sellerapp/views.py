from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.shortcuts import render,redirect
from ecommerceapp.models import *
# Create your views here.
from .forms import *
def register_seller(request):
    if request.method=='POST':
        form=SellerRegistrationForm(request.POST)
        if form.is_valid():
            password=form.cleaned_data.get('password')
            cpassword=form.cleaned_data.get('password')
            if password!=cpassword:
                messages.error(request,"Passwords don't match")
            else:
                user=form.save(commit=False)
                user.set_password(password)
                user.save()
                messages.success(request,'registration successful.you can now log in')
                return HttpResponse('registration success')
    else:
        form=SellerRegistrationForm()
    return render(request,'seller_register.html',{'form':form})



    #
    #         cleaned_data:cleaned_datas refers to the validated datas that has been submitted through form.the form cleaned_data attribute is populated and datas are passes the is_valid method
    #         is_valid:in django is_valid is a method used with forms to check if  the data provided meets  the validation criteria
    #     request.POST which is the method used to pass your POST data into your SellerRegistraionForm
# render else part kondthathite reason
# if the method is not post
# if the form is not valid
# if the password is incorrect
# success

def register_sellers(request):
    return render(request,'seller_register.html',{'form':SellerRegistrationForm()})

def login_view(request):
    if(request.method=="POST"):
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                request.session['sellerid']=user.id
                messages.success(request,f'if you are now logged in as {username}.')
                return redirect(view_seller_upload_product)
            else:
                messages.error(request,'Invalid username or password')
        else:
            messages.error(request,'Invalid username or password')
    else:
        form=AuthenticationForm()
    return render(request,'login.html',{'form':form})




# f=formatter
#           login():function used to login authenticated system
#In django AuthenticationForm is a built-in form class provided by the django.contrib.auth.forms module.
# it is designed to handle user authentication,particularly for logging users into a web app

# When Authenticate() is called ,it checks the provided username and password against
# the user records(models) stored in django authentication system else it returns none

def seller_index(request):
    return render(request,'seller_index.html')



def uploadsellerproduct(request):
    if(request.method=="POST"):
        productname=request.POST.get('productname')
        productprice=request.POST.get('productprice')
        productimage=request.FILES.get('productimage')
        productavailsize=request.POST.get('productavailsize')
        productdescription=request.POST.get('productdescription')
        productcategory=request.POST.get('productcategory')
        data=sellerproductupload(productname=productname,productprice=productprice,productimage=productimage,productavailsize=productavailsize,productdescription=productdescription,productcategory=productcategory)
        data.save()
        return HttpResponse('product details uploaded successfully..........')
    return render(request,'uploadsellerproduct.html')

def view_seller_upload_product(request):
    userid=request.session['sellerid']
    data=User.objects.get(id=userid)
    productcategory=request.GET.get('productcategory','all')
    if productcategory == 'all':
        cart=sellerproductupload.objects.all()
    else:
        cart=sellerproductupload.objects.filter(productcategory=productcategory)
    for item in cart:
        item.productavailsize=item.productavailsize.split(',')

    return render(request,'seller_profile.html',{'data':data,'cart':cart})

def delete_seller_product(request,cartid):
    db=uploadsellerproduct.objects.get(id=cartid)
    db.delete()
    return redirect(seller_profile)





