from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Resume(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	name = models.CharField(max_length=50)

class Personal(models.Model):
	resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
	name = models.CharField(max_length=100)
	occupation = models.CharField(max_length=100,blank=True,null=True)
	objective = models.CharField(max_length=100, default='To be the best in my respective domain!',blank=True,null=True)
	image = models.ImageField(upload_to ='image/',blank=True,null=True)
	nationality = models.CharField(max_length=50,null=True,blank=True) 
	

class About(models.Model):
	resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
	aboutme = models.TextField()

class Hobby(models.Model):
	resume = models.ForeignKey(Resume,on_delete=models.CASCADE)
	name = models.TextField()

class Strength(models.Model):
	resume = models.ForeignKey(Resume,on_delete=models.CASCADE)
	point = models.CharField(max_length=100)

class Weakness(models.Model):
	resume = models.ForeignKey(Resume,on_delete=models.CASCADE)
	point = models.CharField(max_length=100)

class Phone(models.Model):
	resume = models.ForeignKey(Resume,on_delete=models.CASCADE)
	number = models.CharField(max_length=50)

class Email(models.Model):
	resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
	mail = models.CharField(max_length=50)

class Address(models.Model):
	
	resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
	address_type = models.CharField(max_length=100)
	house_no = models.CharField(default='None',max_length=50,blank=True,null=True)
	street =  models.CharField(default='None',max_length=100,blank=True,null=True)
	landmark = models.CharField(default='None',max_length=50,blank=True,null=True)
	city =  models.CharField(max_length=50,blank=True,null=True)
	district = models.CharField(max_length=50,blank=True,null=True)
	state = models.CharField(max_length=50)
	country = models.CharField(max_length=50)
	pin = models.CharField(max_length=50)

class Skill(models.Model):
	
	resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
	skilltype = models.CharField(max_length=50)
	name = models.CharField(max_length=50)  

class Certification(models.Model):
	
	resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
	name = models.CharField(max_length=100)
	mode =  models.CharField(max_length=50)
	link = models.CharField(max_length=100,default='No link',blank=True,null=True)

class Education(models.Model):
	resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
	
	edu_type = models.CharField(max_length=50, default='Under Graduation') 
	institution = models.CharField(default='Awaiting Result', max_length=100)
	affiliation = models.CharField(default='Awaiting Result', max_length=100)
	start = models.IntegerField()
	end = models.IntegerField()
	stream = models.CharField(max_length=100) 
	marks = models.CharField(default='Awaiting Result', max_length=100)

class Employment(models.Model):
	resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
	employer = models.CharField(max_length=100,blank=True,null=True)
	jobtitle = models.CharField(max_length=100,blank=True,null=True)
	jobdesc = models.CharField(max_length=250,blank=True,null=True)
	jobcity = models.CharField(max_length=100,blank=True,null=True)
	jobstate = models.CharField(max_length=100,blank=True,null=True)
	jobstart = models.CharField(max_length=100,blank=True,null=True)
	jobend = models.CharField(max_length=100,blank=True,null=True)

class Social(models.Model):
	resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
	platform = models.CharField(max_length=100)
	name = models.CharField(max_length=100)
	link = models.CharField(max_length=100)

class Project(models.Model):
	resume = models.ForeignKey(Resume, on_delete=models.CASCADE)
	title = models.CharField(max_length=100)
	desc = models.TextField()
	link = models.CharField(default='No Link',max_length=50,blank=True,null=True)
