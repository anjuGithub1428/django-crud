from django.shortcuts import render
from .models import *


# Create your views here.

def home_page( request):
    products=Products.objects.all()

    return render(request,'homepage.html',{"pdts":products})

def login_fn( request):
    admin_username='admin'
    admin_password='123'
    if request.method=='POST':
        username=request.POST.get('username')
        pwd=request.POST.get('pwd')
        
        if admin_username==username and admin_password==pwd:
          return render(request,'success.html')
        else:
          return render(request,'fail.html')   


    return render(request,'login.html')

def sign_fn( request):
    if request.method=='POST':
        name=request.POST.get('name')
        mob=request.POST.get('mob')
        email=request.POST.get('email')
        address=request.POST.get('address')        
        return render(request,'homepage.html',
        {'name':name,'mob':mob,'email':email,'address':address})

    return render(request,'signup.html')

def pdtadd_fn(request):
    if request.method=='POST':
        pdt_name=request.POST.get('pdtname')
        pdt_price=request.POST.get('pdtprice')
        pdt= Products(product_name=pdt_name,product_price=pdt_price)   
        pdt.save()        

    return render(request,'add_product.html')

def studadd_fn(request):
    if request.method=='POST':
        studname=request.POST.get('studname')
        mothername=request.POST.get('mothername')
        fathername=request.POST.get('fathername')
        nationality=request.POST.get('nationality')
        gender=request.POST.get('gender')
        address=request.POST.get('address')
        dob=request.POST.get('dob')
        reserv=request.POST.get('reserv')
        classstd=request.POST.get('class')
        sdt= Students(stud_name=studname,mothername=mothername,fathername=fathername,nationality=nationality,gender=gender,address=address,dob=dob,reserv=reserv,classstd=classstd)   
        sdt.save()

        # messages.add_message(request, messages.INFO, 'Hello world.')
        return render(request,'student_add.html')




    return render(request,'student_add.html')

def studview_fn(request):

     stdt=Students.objects.all()
     return render(request,'student_view.html',{"stdt":stdt})

def updstd_fn(request,id):

    stdt=Students.objects.get(id=id)
    return render(request,'update_stud.html',{"stdt":stdt})

def updstdagain_fn(request):

     if request.method=='POST':
        idd=request.POST.get('id')
        studname=request.POST.get('studname')
        mothername=request.POST.get('mothername')
        fathername=request.POST.get('fathername')
        nationality=request.POST.get('nationality')
        gender=request.POST.get('gender')
        address=request.POST.get('address')
        dob=request.POST.get('dob')
        reserv=request.POST.get('reserv')
        classstd=request.POST.get('class')
        stud_details=Students.objects.get(id= idd)
        stud_details.stud_name=studname
        stud_details.mothername=mothername
        stud_details.fathername=fathername
        stud_details.nationality=nationality
        stud_details.gender=gender
        stud_details.address=address
        stud_details.dob=dob
        stud_details.reserv=reserv
        stud_details.classstd=classstd
        stud_details.save()



     stdt=Students.objects.all()
     return render(request,'student_view.html',{"stdt":stdt})

 

 
