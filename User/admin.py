from django.contrib import admin
from .models import *

# Register your models here.
class tblcontactAdmin(admin.ModelAdmin):
    list_display=("name","email","mobile","message")
admin.site.register(tblcontact,tblcontactAdmin)


class tblgalleryAdmin(admin.ModelAdmin):
    list_display=("title","picture")
admin.site.register(tblgallery,tblgalleryAdmin)


class tblregisterAdmin(admin.ModelAdmin):
    list_display=("name","email","mobile","password","picture","batch","add","regdate")
admin.site.register(tblregister,tblregisterAdmin)


class batchAdmin(admin.ModelAdmin):
    list_display=("id","batch_name")
admin.site.register(batch,batchAdmin)


class tblcategoryAdmin(admin.ModelAdmin):
    list_display=("id","title","picture","batch_name")
admin.site.register(tblcategory,tblcategoryAdmin)


class softwareAdmin(admin.ModelAdmin):
    list_display=("id","title","softinfo","thumbnail","downloadlink","posteddate")
admin.site.register(software,softwareAdmin)

class mylectureAdmin(admin.ModelAdmin):
    list_display=("id","title",'video_info',"vlink","batch","tblcategory","posted_date")
admin.site.register(mylecture,mylectureAdmin)

class notesAdmin(admin.ModelAdmin):
    list_display=( "id","title","notesinfo","batch","posted_date","notesfile")
admin.site.register(notes,notesAdmin)

class mytaskAdmin(admin.ModelAdmin):
    list_display=( "id","title","batch","taskfile","task_info","posted_date")
admin.site.register(mytask,mytaskAdmin)

class submittedtaskAdmin(admin.ModelAdmin):
    list_display=( "id","userid","tid","upload_task","marks","title")
admin.site.register(submittedtask,submittedtaskAdmin)