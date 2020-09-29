from django.shortcuts import render
from django.http import HttpResponse
#from django.http import HttpResponseRedirect
from django.contrib.auth.models import User,auth
from django.contrib.auth import login,logout,authenticate
from django.conf import settings
from django.core.mail import EmailMessage, send_mail
from django.contrib import messages
from .models import CropRegister
from.models import *

global Uname
# write funcions
def home(request):
    return render(request,'Home.html')
def Loginpage(request):
    return render(request,'login.html')
def divpage(request):
    return render(request,'Div.html')
def aboutus(request):
    return render(request,'aboutUs.html')
def contactus(request):
    if request.method=="POST":
        Fname = request.POST['Fname']
        Lname = request.POST['Lname']
        email1 =request.POST['Email']
        textf = request.POST['texta']
        contacts=Contact_us(Fname=Fname,Lname=Lname,email1=email1,textf=textf)
        contacts.save()
        tomail = [email1]
        subject = "welcome to AgorTech Tech"
        body = "Hi, our service team will reach you."
        send_mail(subject, body, settings.EMAIL_HOST_USER, tomail)
        return render(request,'welcome.html')
    else:
        return render(request,'contactus.html')
def consumerpage(request):
    return render(request,'Consumersign.html')
def agentpage(request):
    return render(request,'AgentSignup.html')

def CartPage(request):
    data1=Add_Items.objects.all()
    Allitems = checkout.objects.all()
    cartsize = len(Allitems)
    return render(request,'Cart.html',{'name':data1,'cart':cartsize})

def Addelements(request):
    return render(request,'Addcart.html')

def backpage(request):
    return render(request,'Home.html')

def ItemsCart(request):
    if request.method=='POST'and request.FILES['PFile']:

        ProductId=request.POST['PID']
        ProductName=request.POST['PName']
        ProductImage=request.FILES['PFile']
        FarmerDetails=request.POST['PFarmer']
        Contact_info=request.POST['PInfo']
        Quantity=request.POST['Total']
        Price=request.POST['PPrice']
        Addcart=Add_Items(ProductId=ProductId,ProductName=ProductName,ProductImage=ProductImage,FarmerDetails=FarmerDetails,Contact_info=Contact_info,Quantity=Quantity,
                          Price=Price)
        Addcart.save()
        return render(request,'second.html')
    else:
        return render(request,'Addcart.html')

def feedbackp(request):
    if request.method=='POST':
        Rating=request.POST.get('experience')
        Comments=request.POST['comments']
        Name=request.POST['name']
        Email=request.POST['email']
        feedbackT=Feedback(Rating=Rating,Comments=Comments,Name=Name,Email=Email)
        feedbackT.save()
        Allitems = Add_Items.objects.all()
        tomail = [Email]
        subject = "welcome to AgorTech Tech"
        body = "Hi,\n Our service team will help to solve ur quires"
        send_mail(subject, body, settings.EMAIL_HOST_USER, tomail)
        return render(request,'Cart.html',{'name':Allitems})
    else:
        return render(request,'feedback.html')

def farmerreg(request):
    if request.method == 'POST' and request.FILES['pic']:
        Regnumber = request.POST['NName']
        Fname = request.POST['FName']
        Lname = request.POST['LName']
        Bdate = request.POST['bday']
        #Uname = request.POST['UName']
        Email = request.POST['EId']
        Mobile = request.POST['Mnumber']
        Gender = request.POST.get('Gender')
        Address = request.POST['Address']
        City = request.POST['City']
        Pincode = request.POST['Pcode']
        State = request.POST['State']
        Country = request.POST['Country']
        Tland = request.POST['Landm']
        upimage = request.FILES['pic']
        Ctype = request.POST['Ncrop']
        farmer = FarmerRegister(Regnumber=Regnumber, Fname=Fname, Lname=Lname, Bdate=Bdate,Email=Email,Mobile=Mobile, Gender=Gender, Address=Address, City=City,
                                Pincode=Pincode, State=State, Country=Country, Tland=Tland, upimage=upimage,Ctype=Ctype)
        farmer.save()
        tomail = [Email]
        subject = "welcome to AgorTech Tech"
        body = "hello farmer, welcome to AgroTech.\n,we will assign one agent very soon.\n Thank you for registering us."
        send_mail(subject, body, settings.EMAIL_HOST_USER, tomail)
        return render(request, 'Second.html')
    else:
        return render(request,'farmer.html')

def cropregi(request):
    if request.method == "POST":
        FarmerR = request.POST['number']
        CropI = request.POST['ciname']
        CropN = request.POST['cnname']
        Area = request.POST['aname']
        Typesoil = request.POST['soil']
        WaterS = request.POST['wname']
        Sdate = request.POST['date']
        Edate = request.POST['Edate']
        Loanreq = request.POST.get('loan')
        Ferreq = request.POST.get('pesticides')
        Chec = request.POST.get('har')
        g=FarmerRegister.objects.get(Regnumber=FarmerR)
        crop = CropRegister(farmerRegister=g, CropI=CropI, CropN=CropN, Area=Area, Typesoil=Typesoil, WaterS=WaterS, Sdate=Sdate, Edate=Edate, Loanreq=Loanreq,Ferreq=Ferreq, Chec=Chec)
        crop.save()

        return render(request, 'second.html')
    else:
        return render(request, 'Crop Register.html')


def agentsignin(request):
    if request.method=='POST':
        Fname=request.POST['Fname']
        Lname=request.POST['Lname']
        Email=request.POST['Email']
        Gender=request.POST.get('gender')
        Qualification=request.POST['qualification']
        Ddate=request.POST['ddate']
        IDproof=request.POST['Iname']
        Address=request.POST['region']
        Pincode=request .POST['Pname']
        Password=request.POST['password1']
        Cpassword=request.POST['password2']

        if User.objects.filter(username=Email).exists():
           messages.info(request,'Email already Taken')
           return render(request,'AgentSignup.html')
        else:
            user = User.objects.create_user(username=Email,first_name=Fname,last_name=Lname,password=Password,email=Email)
            agentsign=AgentInfo(Fname=Fname,Lname=Lname,Email=Email,Gender=Gender,Qualification=Qualification,Ddate=Ddate,IDproof=IDproof,Address=Address,
                           Pincode=Pincode)
            agentsign.save()
            tomail = [Email]
            subject = "welcome to AgorTech Tech"
            body = "we willl serve you more"
            send_mail(subject, body, settings.EMAIL_HOST_USER, tomail)

        return render(request,'login.html')
    else:
        return render(request,'Div.html')

def consumersignin(request):
    if request.method=='POST':
        Fname=request.POST['Fname']
        Lname=request.POST['Lname']
        Email=request.POST['Email']
        Gender=request.POST.get('gender')
        Qualification=request.POST['qualification']
        Ddate=request.POST['ddate']
        IDproof=request.POST['Iname']
        Address=request.POST['region']
        Pincode=request.POST['Pname']
        Password=request.POST['password1']
        Cpassword = request.POST['password2']

        if User.objects.filter(username=Email).exists():
           messages.info(request,'Email already Taken')
           return render(request, 'Consumersign.html')
        else:
            user = User.objects.create_user(username=Email, first_name=Fname, last_name=Lname, password=Password,email=Email)

            consumersign=ConsumerInfo(Fname=Fname,Lname=Lname,Email=Email,Gender=Gender,Qualification=Qualification,Ddate=Ddate,IDproof=IDproof,Address=Address,
                                 Pincode=Pincode)
            consumersign.save()

            tomail = [Email ]
            subject = "welcome to AgorTech Tech"
            body = "we willl serve you more"
            send_mail(subject, body, settings.EMAIL_HOST_USER, tomail)

            return render(request,'login.html')
    else:
        return render(request,'Div.html')
def login(self):
    if self.method=='POST':
        Uname=self.POST['Uname']
        password=self.POST['password']
        user=auth.authenticate(username=Uname,password=password)
        if user is not None:
            auth.login(self,user)

            return render(self,'second.html',{'un':Uname})
        else:
            return render(self,'login.html' )
    else:
        return render(self, 'Home.html')
def Thankyou1(request):
    return render(request,'second.html')

def logout1(request):
    auth.logout(request)
    return render(request,'Home.html')

def fetchfarmer(request):
    Allfarmers=FarmerRegister.objects.all()
    return render(request,'FetchFarmer.html',{'farmers':Allfarmers})

def fetchagent(request):
    AllAgent=AgentInfo.objects.all()
    return render(request,'AgentFetch.html',{'agent':AllAgent})

def fetchconsumer(request):
    AllConsumer=ConsumerInfo.objects.all()
    return render(request,'Consumerfetch.html',{'consumer':AllConsumer})

def fetchcontact(request):
    Allcontact=Contact_us.objects.all()
    return render(request,'contactfetch.html',{'contact':Allcontact})

def Feedback1(request):
    Allfeedback=Feedback.objects.all()
    return render(request,'Feedbackfetch.html',{'feedback':Allfeedback})

def cropfetch(request):
    Allcrop=CropRegister.objects.all()
    return render(request,'cropfetch.html',{'crop':Allcrop})

def CartSignup(request):
    if request.method=='POST':
        Fname=request.POST['Name']
        Email=request.POST['email']
        Address=request.POST['Address']
        Pass=request.POST['psw']
        Cpass= request.POST['psw-repeat']

        if User.objects.filter(username=Email).exists():
            messages.info(request,'Email already Taken')
            return render(request,'Cartsignup.html')
        else:
            cart = User.objects.create_user(username=Email, first_name=Fname, password=Pass)
            sign=CartUser(UserName=Fname,Email=Email,Address=Address)
            sign.save()
            tomail = [Email]
            subject = "welcome to AgorTech Tech"
            body = "Welcome to AgroTech Cart,\nBest people choose AgroTech \nBest people always Deserve the Best."
            send_mail(subject, body, settings.EMAIL_HOST_USER, tomail)

        return render(request,'CartLogin.html')
    else:
        return render(request,'CartSignup.html')

def Cartsignup(request):
    return render(request,'CartSignUp.html')

def CartLogin(self):
    if self.method=='POST':
        username=self.POST['email']
        password=self.POST['psw']
        cart=auth.authenticate(username=username,password=password)
        if cart is not None:
            auth.login(self,cart)
            Allitems = checkout.objects.all()
            return render(self,'checkout.html',{'un':username,'items':Allitems})
        else:
            Allitems = checkout.objects.all()
            return render(self,'checkout.html',{'un':username,'items':Allitems} )
    else:
        return render(self, 'CartLogin.html')

def Checkout(request):
    if request.method=="POST":
        ProductId=request.POST['productno']
        Productprice=request.POST['price1']
        ProductName=request.POST['pname']
        items=checkout(ProductId=ProductId,ProductName=ProductName,Productprice=Productprice)
        items.save()
        ItemsinBag=Add_Items.objects.all()

        Allitems = checkout.objects.all()
        cartsize = len(Allitems)
        return render(request,'Cart.html',{'name':ItemsinBag,'cart':cartsize})
    else:
        return render(request, 'Crop Register.html')

def itemout(request):
    Allitems=checkout.objects.all()
    return render(request,'checkout.html',{'items':Allitems})


def Removeitems(request):
    ProductId=request.POST['pid']
    k=checkout.objects.get(ProductId=ProductId)
    k.delete()
    Allitems = checkout.objects.all()
    return render(request, 'checkout.html', {'items': Allitems})


