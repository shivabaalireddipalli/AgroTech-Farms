
from django.db import models

# Create your models here.

class Contact_us(models.Model):
    Fname=models.CharField(max_length=30)
    Lname=models.CharField(max_length=30)
    email1=models.EmailField(max_length=30)
    textf=models.EmailField(max_length=30)

class AgentInfo(models.Model):
    Fname=models.CharField(max_length=30)
    Lname=models.CharField(max_length=30)
    Email=models.CharField(max_length=30)
    Gender=models.CharField(max_length=30)
    Qualification=models.CharField(max_length=30)
    Ddate=models.DateField(max_length=30)
    IDproof=models.CharField(max_length=30)
    Address=models.CharField(max_length=100)
    Pincode=models.IntegerField(default=0)


class ConsumerInfo(models.Model):
    Fname = models.CharField(max_length=30)
    Lname = models.CharField(max_length=30)
    Email = models.CharField(max_length=30)
    Gender = models.CharField(max_length=30)
    Qualification = models.IntegerField()
    Ddate = models.DateField(max_length=30)
    IDproof = models.CharField(max_length=30)
    Address = models.CharField(max_length=100)
    Pincode=models.IntegerField(default=None)


class Add_Items(models.Model):
    ProductId=models.IntegerField(default=None,primary_key=True)
    ProductName=models.CharField(max_length=30)
    ProductImage=models.FileField(upload_to='documents/')
    FarmerDetails = models.CharField(max_length=30)
    Contact_info = models.CharField(max_length=30)
    Quantity=models.IntegerField(default=None)
    Price = models.FloatField()


class Feedback(models.Model):
    Rating=models.CharField(max_length=30)
    Comments=models.CharField(max_length=30)
    Name=models.CharField(max_length=30)
    Email=models.CharField(max_length=30)


class FarmerRegister(models.Model):
    Regnumber=models.IntegerField(default=None,primary_key=True)
    Fname=models.CharField(max_length=30)
    Lname=models.CharField(max_length=30)
    Bdate=models.DateField()
    #Uname=models.CharField(max_length=30)
    Email=models.EmailField()
    Mobile=models.IntegerField()
    Gender=models.CharField(max_length=30)
    Address=models.CharField(max_length=30)
    City=models.CharField(max_length=30)
    Pincode=models.IntegerField()
    State=models.CharField(max_length=30)
    Country=models.CharField(max_length=30)
    Tland=models.IntegerField()
    upimage=models.FileField(upload_to='documents/')
    Ctype=models.CharField(max_length=30)

class CropRegister(models.Model):
    farmerRegister=models.ForeignKey(FarmerRegister, on_delete=models.CASCADE)
    CropI=models.IntegerField()
    CropN=models.CharField(max_length=30)
    Area=models.FloatField()
    Typesoil=models.CharField(max_length=30)
    WaterS=models.CharField(max_length=30)
    Sdate=models.DateField(auto_now_add=True)
    Edate=models.DateField()
    Loanreq=models.CharField(max_length=30)
    Ferreq=models.CharField(max_length=30)
    Chec=models.CharField(max_length=30,default='0')

class Seconddata(models.Model):
    Today=models.CharField(max_length=30)
    Head=models.CharField(max_length=250)
    img=models.CharField(max_length=250)
    quote=models.CharField(max_length=250)
    subquote=models.CharField(max_length=250)

class checkout(models.Model):
    user=models.CharField(max_length=30,default='0')
    ProductId=models.IntegerField(default=None,primary_key=True)
    ProductName=models.CharField(max_length=30,default='0')
    Productprice= models.FloatField(default=None)

class CartUser(models.Model):
    UserName=models.CharField(max_length=30,default='0')
    Email=models.EmailField()
    Address=models.CharField(max_length=30)



