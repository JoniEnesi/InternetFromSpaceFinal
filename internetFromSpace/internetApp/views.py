import uuid
from django.conf import settings
from django.shortcuts import render, redirect
from django.urls import reverse
from internetApp.models import *
from django.contrib import messages
from .forms import *
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from .models import *
from django.contrib.auth.decorators import login_required
from paypal.standard.forms import PayPalPaymentsForm





# Create your views here.
def homeFun(request):
    return render(request, 'home.html')

def aboutFun(request):
    return render(request, 'About.html')

def worksFun(request):
    return render(request, 'how_it_works.html')

def contactFun(request):
    message = Message.objects.all()

    if request.method == "POST":
        emri = request.POST['msgemri']
        mbiemri = request.POST['msgmbiemri']
        email = request.POST['email']
        message = request.POST['msg']

        if emri !='' and mbiemri !='' and email !='' and message !='':
            Message(message_name = emri, message_surname = mbiemri, message_email = email, message_comment = message).save()
            messages.success(request, "Your message is sended!")
        else:
            messages.warning(request, "Message not send!")

    context = {'message':message}
    return render(request, 'contact.html', context)

def priceFun(request):
    prices = Price.objects.all()
    pricess = PriceBusiness.objects.all()

    context = {'prices':prices, 'pricess':pricess}
    return render(request, 'pricing.html', context)

@login_required(login_url='singup')
def priceProduct(request, slug):
    detProduct = Price.objects.get(slug=slug)

    if request.method == 'POST':
        emri = request.POST['res_emri']
        mbiemri = request.POST['res_mbiemri']
        email = request.POST['res_email']
        number = request.POST['res_number']
        address = request.POST['res_address']
        street = request.POST['res_street']

        if emri != '' and mbiemri != '' and email != '' and number != '' and address != '' and street != '':
            Reservation(reservation_name=emri, reservation_lastname=mbiemri, reservation_email=email,
                        reservation_phone=number, reservation_address=address, reservation_street=street,
                        reservation_paket=detProduct, user=request.user).save()
            messages.success(request, "Your reservation is sended, Pay Now!"),
            return redirect('pay', slug=slug)
        else:
            messages.warning(request, "Reservation not send!")

    context = {'detProduct':detProduct}
    return render(request, 'price_product.html', context)

def payFun(request, slug):
    detProduct = Price.objects.get(slug=slug)
    host = request.get_host()

    paypal_dict ={
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': detProduct.internet_price,
        'item_name': detProduct.slug,
        'invoice': str(uuid.uuid4()),
        'currency_code': 'USD',
        'notify_url': f'http://{host}{reverse("paypal-ipn")}',
        'return_url': f'http://{host}{reverse("paypal-reverse")}',
        'cancel_return': f'http://{host}{reverse("paypal-cancel")}',
    }

    form = PayPalPaymentsForm(initial=paypal_dict)

    context = {'detProduct':detProduct, 'form':form}
    return render(request, 'pay.html', context)

@login_required(login_url='singup')
def priceProductBusiness(request, slug):
    detProduct_Business = PriceBusiness.objects.get(slug=slug)

    if request.method == 'POST':
        emri = request.POST['res_emri']
        mbiemri = request.POST['res_mbiemri']
        email = request.POST['res_email']
        number = request.POST['res_number']
        address = request.POST['res_address']
        street = request.POST['res_street']

        if emri !='' and mbiemri !='' and email !='' and number !='' and address !='' and street !='':
            Reservation(reservation_name = emri, reservation_lastname = mbiemri, reservation_email = email, reservation_phone = number, reservation_address = address, reservation_street = street, reservation_paketBusiness = detProduct_Business, user = request.user).save()
            messages.success(request, "Your reservation is sended, Pay Now!")
            return redirect('paybusiness', slug=slug)
        else:
            messages.warning(request, "Reservation not send!")

    context = {'detProduct_Business':detProduct_Business}
    return render(request, 'price_category.html', context)


def payFunBusiness(request, slug):
    detProduct_Business = PriceBusiness.objects.get(slug=slug)
    host = request.get_host()

    paypal_dict ={
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': detProduct_Business.internet1_price,
        'item_name': detProduct_Business.slug,
        'invoice': str(uuid.uuid4()),
        'currency_code': 'USD',
        'notify_url': f'http://{host}{reverse("paypal-ipn")}',
        'return_url': f'http://{host}{reverse("paypal-reverse")}',
        'cancel_return': f'http://{host}{reverse("paypal-cancel")}',
    }

    form = PayPalPaymentsForm(initial=paypal_dict)

    context = {'detProduct_Business':detProduct_Business, 'form':form}
    return render(request, 'pay_business.html', context)

def singupFun(request):

    if request.method == "POST":
        form = login_form(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                messages.success(request, "You are login!")
                auth.login(request, user)
                return redirect('home')
        else:
            messages.warning(request, "Your username or password is incorrect!")


    form = login_form()
    context = {'form':form}


    return render(request, 'user/singup.html', context)

def registerFun(request):

    if request.method == 'POST':
        form = register(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "You are registered! Now you can Sing Up!")
            return redirect('home')
    else:
        form = register()
    context = {'form': form}

    return render(request, 'user/register.html', context)


def logout(request):
    messages.info(request, "You are logout!")
    auth.logout(request)
    return  render(request, 'home.html')

def internetFun(request):
    return render(request, 'Internetisland.html')

def innovationFun(request):
    return render(request, 'innovation.html')

def cyberFun(request):
    return render(request, 'cybersecurity.html')

def paypal_reverse(request):
    messages.success(request, 'You\'ve successfully have payment!')
    return redirect('price')

def paypal_cancel(request):
    messages.warning(request, 'Your order have been cancelled')
    return redirect('price')
