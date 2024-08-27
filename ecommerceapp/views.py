from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse
from django.conf import settings
import stripe
from datetime import datetime,timedelta
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request,'index.html')

def Userregistration(request):
    if(request.method=='POST'):
        fullname=request.POST.get('fullname')
        email=request.POST.get('email')
        gender=request.POST.get('gender')
        phone=request.POST.get('phone')
        propic=request.FILES.get('propic')
        password=request.POST.get('password')
        cpassword=request.POST.get('cpassword')
        if(password==cpassword):
            data=userregister(fullname=fullname,email=email,gender=gender,phone=phone,propic=propic,password=password)
            data.save()
            return redirect(Userlogin)
        else:
            return HttpResponse('registration failed')

    return render(request,'registration.html')
def Userlogin(request):
    if(request.method=='POST'):
        email=request.POST.get('email')
        password=request.POST.get('password')
        data=userregister.objects.all()
        for i in data:
            if(i.email==email and i.password==password):
                request.session['userid']=i.id
                return redirect(userprofile)
        else:
            return HttpResponse('login failed')
    return render(request,'userlogin.html')

def userprofile(request):


    # if there is no categroy is selected all option will work
    id1=request.session['userid']
    data=userregister.objects.get(id=id1)


    return render(request,'userprofile.html',{'data':data})

def viewdetails(request):
    id1=request.session['userid']
    data=userregister.objects.get(id=id1)
    return render(request,'viewdetails.html',{'data':data})

def updateuserdetails(request):
    id1=request.session['userid']
    data=userregister.objects.get(id=id1)
    if(request.method=='POST'):
        data.fullname=request.POST.get('fullname')
        if(request.FILES.get('propic')==None):
            data.save()
        else:
            data.propic=request.FILES.get('propic')
        data.email=request.POST.get('email')
        data.phone=request.POST.get('phone')
        data.gender=request.POST.get('gender')
        data.save()
        return redirect(userprofile)
    return render(request,'updateuserdetails.html',{'data':data})

# def uploadsellerproduct(request):
#     if(request.method=="POST"):
#         productname=request.POST.get('productname')
#         productprice=request.POST.get('productprice')
#         productimage=request.FILES.get('productimage')
#         productavailsize=request.POST.get('productavailsize')
#         productdescription=request.POST.get('productdescription')
#         productcategory=request.POST.get('productcategory')
#         data=sellerproductupload(productname=productname,productprice=productprice,productimage=productimage,productavailsize=productavailsize,productdescription=productdescription,productcategory=productcategory)
#         data.save()
#         return HttpResponse('product details uploaded successfully..........')
#     return render(request,'uploadsellerproduct.html')

def addtocart(request,itemid):
    item=sellerproductupload.objects.get(id=itemid)
    cart=CartItem.objects.all()
    productavailsize=''
    if(request.method=='GET'):
        productavailsize = request.GET.get('productavailsize')
    for i in cart:
        if i.item.id==itemid and i.selected_size==productavailsize and i.userid==request.session['userid']:
            i.quantity+=1
            i.save()
            return redirect(cartdisplay)
    else:
            db=CartItem(userid=request.session['userid'],item=item,selected_size=productavailsize)
            db.save()
            return redirect(cartdisplay)
def viewproducts(request):
    try:
        id1=request.session['userid']
        data=userregister.objects.get(id=id1)
        productcategory = request.GET.get('productcategory', 'all')
        if productcategory == 'all':
            db = sellerproductupload.objects.all()
        else:
            db = sellerproductupload.objects.filter(productcategory=productcategory)
        for item in db:
            item.productavailsize = item.productavailsize.split(',')
        return render(request,'viewproducts.html',{'db':db,'data':data})
    except KeyError:
        return redirect(Userlogin)


def cartdisplay(request):
    userid=request.session['userid']
    db=CartItem.objects.filter(userid=userid)
    total=0
    count=0
    for i in db:
        i.item.productprice*=i.quantity
        total+=i.item.productprice
        count+=1
    return render(request,'cartdisplay.html',{'db':db,'total':total,'count':count})

def incdec(request,cartid):
    db=CartItem.objects.get(id=cartid)
    action=request.GET.get('action')
    if action=='increment':
        db.quantity+=1
        db.save()
    elif action=='decrement' and db.quantity>1:
        db.quantity-=1
        db.save()
    return redirect(cartdisplay)

def deletecart(request,cartid):
    db=CartItem.objects.get(id=cartid)
    db.delete()
    return redirect(viewproducts)

def wishlist(request,itemid):
    item=sellerproductupload.objects.get(id=itemid)
    cart=WishList.objects.all()
    for i in cart:
        if i.item.id==itemid and i.userid==request.session['userid']:
            i.save()
            return HttpResponse('item added to wishlist')
    else:
        db=WishList(userid=request.session['userid'],item=item)
        db.save()
        return HttpResponse('item already in wishlist')

def wishlistdisplay(request):
    id=request.session['userid']
    db=WishList.objects.filter(userid=id)
    #data preprocess
    for i in db:
        i.item.productavailsize=i.item.productavailsize.split(',')
        print(i.item.productavailsize)
    return render(request,'wishlist.html',{'db':db})
def add_address(request):
    id1=request.session['userid']
    userdata=userregister.objects.get(id=id1)
    if(request.method=='POST'):
        address_line1=request.POST.get('address_line1')
        address_line2=request.POST.get('address_line2')
        pincode=request.POST.get('pincode')
        city=request.POST.get('city')
        state=request.POST.get('state')
        contact_name=request.POST.get('contact_name')
        contact_number=request.POST.get('contact_number')
        data=Address_details(userdetails=userdata,address_line1=address_line1,address_line2=address_line2,pincode=pincode,city=city,state=state,contact_name=contact_name,contact_number=contact_number)
        data.save()
        return redirect(delivaryaddress)
    else:
        return render(request,'add_address.html')

def delete_from_wishlist(request,wishid):
    db=WishList.objects.get(id=wishid)
    db.delete()
    return redirect(wishlist)
def delivaryaddress(request):
    userid=request.session['userid']
    data=Address_details.objects.filter(userdetails__id=userid)
    return render(request,'delivaryaddress.html',{'data':data})

def summarypage(request):
    userid=request.session['userid']
    address_id=request.GET.get('address')
    address=Address_details.objects.get(id=address_id)
    item=CartItem.objects.filter(userid=userid)
    key=settings.STRIPE_PUBLISHABLE_KEY
    total=0
    striptotal = 0
    for i in item:
        i.item.productprice*=i.quantity
        total+=i.item.productprice
        striptotal=total*100
        return render(request,'summarypage.html',{'address':address,'item':item,'total':total,'key':key,'striptotal':striptotal})
#      after payment
def create_order(request):
    if (request.method=='POST'):
        order_items=[]
        total_price=0
        userid=request.session['userid']
        # user session calling
        user=userregister.objects.get(id=userid)
        address_id=request.POST.get('address_id')
        address=Address_details.objects.get(id=address_id)
        cart=CartItem.objects.filter(userid=userid)
        order=Order.objects.create(userdetails=user,address=address)
#         automatically save not using order.save()
        for i in cart:
            OrderItem.objects.create(
                order=order,
                order_pic=i.item.productimage,
                pro_name=i.item.productname,
                quantity=i.quantity,
                price=i.item.productprice
            #     for model
            )
            total_price+=i.item.productprice*i.quantity
            order_items.append({
                'productname':i.item.productname,
                'quantity':i.quantity,
                'productprice':i.item.productprice*i.quantity
            #     for mail
            })
        expected_delivery_date=datetime.now()+timedelta(days=7)
        # import datetime
        # Construct email content
        subject='Order Confirmation'
        context={
            'order_items':order_items,
            # list of items
            'total_price':total_price,
            # total price
            'expected_delivery_date':expected_delivery_date.strftime('%y-%m-%d')
        }
        html_message=render_to_string('order_confirmation_email.html',context)
        plain_message=strip_tags(html_message)
        from_email='lakshmikishore008@gmail.com'
        to_email=[user.email]
        send_mail(subject,plain_message,from_email,to_email,html_message=html_message)
        # subject variable,plain_message,from_email,to_email,(html=htm_message)
        cart.delete()
        return HttpResponse('order created successfully')

def orderview(request):
    userid=request.session['userid']
    order=OrderItem.objects.filter(order__userdetails__id=userid).order_by('-order__ordered_date')
    return render(request,'orderview.html',{'order':order})
# which is used

def order_cancel(request,id):
    userid=request.session['userid']
    user = userregister.objects.get(id=userid)
    db=OrderItem.objects.get(id=id)
    db.order_status=False
    db.save()
    subject = 'Order Cancellation'
    context = ({'pro_name':db.pro_name,
                'price': db.price})
    html_message=render_to_string('order_cancellation.html',context)
    plain_message=strip_tags(html_message)
    from_email='lakshmikishore008@gmail.com'
    to_email=[user.email]
    send_mail(subject,plain_message,from_email,to_email,html_message=html_message)

    return HttpResponse('order cancelled')
def samplecard(request):
    return render(request,'samplecard.html')

def change_password_user(request):
    userid=request.session['userid']
    data=userregister.objects.get(id=userid)
    if(request.method=='POST'):
        oldpassword=request.POST.get('oldpassword')
        newpassord=request.POST.get('newpassword')
        retype=request.POST.get('retype')
        if(data.password==oldpassword):
            if (newpassord == retype):
                data.password=request.POST.get('newpassword')
                data.save()
                return redirect(Userlogin)
            else:
                return HttpResponse('password dont match')
        else:
            return HttpResponse('Enter correct password')
    return render(request,'change_password_user.html')

def logout(request):
    request.session.flush()
    return redirect(Userlogin)


