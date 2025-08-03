from django.shortcuts import render,redirect
from User.models import *
from django.http import HttpResponse
# Create your views here.
def dashboard(request):
  return render(request, "student/dashboard.html")
def enotes(request):
    bid=request.session.get("batch")
    data=notes.objects.all().filter(batch=bid)
    d={"notes":data}
    return render(request,"student/enotes.html",d)



def profile(request):
    user=request.session.get("email")
    data=tblregister.objects.all().filter(email=user)
    d={"userinfo":data}
    return render(request,"student/profile.html",d)

def mycategory(request):
    
    return render(request,"student/category.html")
def signout(request):
    student=request.session.get("email")
    if student:
        del request.session["email"]
        return redirect("/login/")
    return render(request,"student/signout.html")

def softkit(request):
    data=software.objects.all().order_by("-id")
    return render(request,"student/softkit.html",{"sdata":data})
def category(request):
    x=request.GET.get("cid")
    if x:
      data=mylecture.objects.all().filter(category=x)
    else:
        data=mylecture.objects.all().order_by("-id")
    d={"vdo":data}
    return render(request,"student/lectures.html",d)
def lectures(request):
    x=request.GET.get("cid")
    if x:
      data=mylecture.objects.all().filter(tblcategory=x)
    else:
        data=mylecture.objects.all().order_by("-id")
    d={"vdo":data}
    return render(request,"student/lectures.html",d)

def lecturecat(request):
    bid=request.session.get("batch")
    cat=tblcategory.objects.all().filter(batch_name=bid)
    d={"categories":cat}
    return render(request,"student/lecturecat.html",d)

def task(request):
    bid=request.session.get("batch")
    data=mytask.objects.all().filter(batch=bid)
    d={"data":data}
    return render(request,"student/task.html",d)

def tsubmitted(request):
    userid=request.session.get("email")
    if request.method=="POST":
        title=request.POST.get("title")
        tid=request.POST.get("tid")
        taskfile=request.FILES["fu"]
        x=submittedtask.objects.all().filter(userid=userid,tid=tid).count()
        if x==1:
            return HttpResponse("<script>alert('this task is already submitted');location.href='/student/task/'</script>")
        else :
            submittedtask(title=title,tid=tid,upload_task=taskfile,userid=userid).save()
            return HttpResponse("<script>alert('this  submitted successfully ');location.href='/student/task/'</script>")
    return render(request,"student/tsubmitted.html")






