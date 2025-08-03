from django.db import models

# Create your models here.
  
class batch(models.Model):
  batch_name=models.CharField(max_length=40,null=True)
  def __str__(self): #show name of batch beacuse waha pe name na dikhakar batch object dikhata hai
    return self.batch_name

# Create table tblcontact
class tblcontact(models.Model):
  # store data
  name=models.CharField(max_length=70,null=True)
  email=models.EmailField(max_length=100,null=True)
  mobile=models.CharField(max_length=20,null=True)
  message=models.TextField(null=True)
# store and change gallery images and make dynamic pic
# note jab bhi hm kisi image par kam karenge to ek module install karna padta hai jiska nam pillow hai yah predefine hota hai 
#pip install pillow
class tblgallery(models.Model):
  title=models.CharField(max_length=50)
# select image and move to static/gallery folder

  picture=models.ImageField(upload_to="static/gallery/", null=True)
  
# yah abhi bana nhi hai esko banane ke liye do command ka use karna hota hai 1 
class tblteam(models.Model):
  title=models.CharField(max_length=50)
  profession=models.CharField(max_length=70)
  picture=models.ImageField(upload_to="static/gallery/", null=True)
  
#register section
class tblregister(models.Model):
  name=models.CharField(max_length=50, null=True)
  email=models.EmailField(primary_key=True,max_length=100)
  mobile=models.CharField(max_length=20, null=True)
  password=models.CharField(max_length=30,null=True)
  picture=models.ImageField(upload_to="static/userpic/",blank=True,null=True)
  batch=models.ForeignKey(batch,on_delete=models.CASCADE, null=True)
  add=models.TextField(null=True)
  regdate=models.DateField(null=True)

class software(models.Model):
  title=models.CharField(max_length=100,null=True)
  softinfo=models.TextField(null=True)
  thumbnail=models.ImageField(upload_to="softthumb/",null=True)
  downloadlink=models.CharField(max_length=200,null=True)
  posteddate=models.DateField(null=True)
  
  
class tblcategory(models.Model):
  title=models.CharField(max_length=30, null=True)
  picture=models.ImageField(upload_to="static/category/", null=True,blank=True)
  batch_name=models.ForeignKey(batch,on_delete=models.CASCADE)
  def __str__(self): #show name of batch beacuse waha pe name na dikhakar batch object dikhata hai
    return self.title

class mylecture(models.Model):
  title=models.CharField(max_length=200,null=True)
  video_info=models.TextField(null=True)
  vlink=models.CharField(max_length=300,null=True)
  batch=models.ForeignKey(batch,on_delete=models.CASCADE,null=True)
  tblcategory=models.ForeignKey(tblcategory,on_delete=models.CASCADE,null=True)
  posted_date=models.DateTimeField(null=True)
  
  
class notes(models.Model):
  title=models.CharField(max_length=200,null=True)
  notesinfo=models.TextField(null=True)
  batch=models.ForeignKey(batch,on_delete=models.CASCADE,null=True)
  posted_date=models.DateTimeField(null=True)
  notesfile=models.FileField(upload_to="static/notes/",null=True)
  
class mytask(models.Model):
    title=models.CharField(max_length=300,null=True)
    task_info=models.TextField(null=True)
    batch=models.ForeignKey(batch,on_delete=models.CASCADE)
    taskfile=models.FileField(upload_to="static/task/",null=True,blank=True)
    posted_date=models.DateField(null=True)

class submittedtask(models.Model):
    userid=models.CharField(max_length=50,null=True)
    tid=models.IntegerField(null=True)
    title=models.CharField(max_length=50,null=True)
    upload_task=models.FileField(upload_to="static/submitted/",null=True,blank=True)
    marks=models.IntegerField(null=True)
   