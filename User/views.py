from django.shortcuts import render
from django.http import HttpResponse
from .models import * # import table
from datetime import datetime #import current date time for usingform
# Create your views here.
def index(request): #get value and store in variables
    if request.method=="POST":
      Name=request.POST.get("name")
      Mobile=request.POST.get("mob")
      Email=request.POST.get("email")
      Message=request.POST.get("msg")
      tblcontact(name=Name,email=Email,mobile=Mobile,message=Message).save()#fieldname=store hone wali data
      return HttpResponse("<script>alert('data saved succsesfully');location.href='/index/'</script>")
    return render(request,"index.html")
def about(request):
    return render(request,"about.html")
def team(request):
    data=tblteam.objects.all()
    d={"team":data}
    return render(request,"team.html",d)
def gallery(request):
    data=tblgallery.objects.all()
    d={"gal":data}
    return render(request,"gallery.html",d)
def services(request):
    return render(request,"services.html")
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        # Optionally save to DB or send email here
        print(name, email, subject, message)  # Just for testing

        messages.success(request, "Thank you! Your message has been sent.")
        return render(request, 'contact.html')  # same page reload
    return render(request, 'contact.html')

def login(request):
    if request.method=="POST":
        Email=request.POST.get("email")
        Passwd=request.POST.get("password")
        x=tblregister.objects.all().filter(email=Email,password=Passwd)
        if x.count()==1:
            
             request.session["name"]=str(x[0].name)
             request.session["userpic"]=str(x[0].picture)
             
             request.session["email"]=Email
             
             if "batch" in request.session:
                 del request.session["batch"]
             b=x[0].batch
             if b:
                request.session["batch"]=str(x[0].batch.id)
             
             return HttpResponse("<script>alert('login succsesfully');location.href='/student/dashboard/'</script>")
        else:
             return HttpResponse("<script>alert('Your Email or Password is incorrect ');location.href='/login/'</script>")
    return render(request,"login.html")
def register(request):
    if request.method=="POST":
      N=request.POST.get("name")
      E=request.POST.get("email")
      M=request.POST.get("mob")
      P=request.POST.get("password")
      pic=request.FILES["fu"]
      A=request.POST.get("add")
      D=request.POST.get("regdate")
      #store tblregister table
      tblregister(name=N,email=E,mobile=M,password=P,picture=pic,add=A,regdate=datetime.now().date()).save()
      return HttpResponse("<script>alert('you are register succsesfully');location.href='/index/'</script>")
    return render(request,"register.html")
    

