from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    full_name = models.CharField(max_length=255, blank=True)
    email= models.EmailField(unique=True)
    dob= models.DateField(null=True,blank=True)
    date_of_join= models.DateField(null=True,blank=True)
    reporting_to = models.ForeignKey("User", on_delete=models.CASCADE, null=True)
    contact_number = models.CharField(max_length=12)
    emergency_contact_number = models.CharField(max_length=12)
    position = models.CharField(max_length=100,blank=True)
    marital_status = models.CharField(max_length=100,blank=True)
    blood_group = models.CharField(max_length=10)
    job_title = models.CharField(max_length=100, blank=True)
    work_location = models.CharField(max_length=150, blank=True)
    linkedin_link = models.URLField()
    profile_pic = models.ImageField(upload_to="media/",blank=True, null=True)


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

class Leave(models.Model):
    employeeName= models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    applyDate= models.DateField()
    natureOfLeave= models.CharField(max_length=100)
    firstDay= models.DateField()
    lastDay= models.DateField()
    numberOfDays= models.PositiveIntegerField()
    status= models.CharField(max_length=100,default="pending")