from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User


# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

@login_required(login_url='registerview')
def add_information(request):
    return render(request,'add_information.html')

@login_required(login_url='registerview')
def select_template(request):
    return render(request,'select_template.html')


def loginview(request):
    return render(request, 'login.html')




def registerview(request):
	return render(request,'register.html')


def loginuser(request):
	if request.method == "POST":

		username = request.POST.get('username')
		password = request.POST.get('password')

		print("got creden")

		user = authenticate(request, username=username, password=password)
		print("authemticated")
		if user is not None:
			login(request,user)
			return redirect('index')
		else:
			return redirect('index')

	return redirect('index')


def registeruser(request):
	if request.method == "POST": 
		username = request.POST.get('username')
		email = request.POST.get('email')
		password = request.POST.get('password')

		user = User.objects.create(username=username, email=email)
		user.set_password(password)
		user.save()
		return redirect('loginview')

	else:

		return render(request,'register.html')

	return render(request,'register.html')

def logoutuser(request):
	logout(request)
	return redirect('registerview')



def ai(request):
	username = 'admin'
	user = User.objects.get(username=username)
	resume = Resume.objects.filter(user=user).first()
	personal = Personal.objects.filter(resume=resume)
	about = About.objects.filter(resume=resume)
	hobby = Hobby.objects.filter(resume=resume)
	strength = Strength.objects.filter(resume=resume)
	weakness = Weakness.objects.filter(resume=resume)
	email = Email.objects.filter(resume=resume)

	phone = Phone.objects.filter(resume=resume)
	address = Address.objects.filter(resume=resume)
	skill = Skill.objects.filter(resume=resume)
	certification = Certification.objects.filter(resume=resume)
	education = Education.objects.filter(resume=resume)
	employment = Employment.objects.filter(resume=resume) 
	social = Social.objects.filter(resume=resume)
	project = Project.objects.filter(resume=resume)

	context = {'personal':personal,'about':about,'hobby':hobby,'strength':strength,'weakness':weakness,
	'email':email,'education':education,'phone':phone,'address':address,'skill':skill,'certification':certification,
	'employment':employment,'social':social,'project':project}

	return render(request,'ai.html', context)


def eps(request):
	user = request.user
	resume = Resume.objects.filter(user=user).first()
	personal = Personal.objects.filter(resume=resume)
	about = About.objects.filter(resume=resume)
	hobby = Hobby.objects.filter(resume=resume)
	strength = Strength.objects.filter(resume=resume)
	weakness = Weakness.objects.filter(resume=resume)
	email = Email.objects.filter(resume=resume)

	phone = Phone.objects.filter(resume=resume)
	address = Address.objects.filter(resume=resume)
	skill = Skill.objects.filter(resume=resume)
	certification = Certification.objects.filter(resume=resume)
	education = Education.objects.filter(resume=resume)
	employment = Employment.objects.filter(resume=resume) 
	social = Social.objects.filter(resume=resume)
	project = Project.objects.filter(resume=resume)

	context = {'personal':personal,'about':about,'hobby':hobby,'strength':strength,'weakness':weakness,
	'email':email,'education':education,'phone':phone,'address':address,'skill':skill,'certification':certification,
	'employment':employment,'social':social,'project':project}

	return render(request,'eps.html', context)

def psd(request):
	username = 'admin'
	user = User.objects.get(username=username)
	resume = Resume.objects.filter(user=user).first()
	personal = Personal.objects.filter(resume=resume)
	about = About.objects.filter(resume=resume)
	hobby = Hobby.objects.filter(resume=resume)
	strength = Strength.objects.filter(resume=resume)
	weakness = Weakness.objects.filter(resume=resume)
	email = Email.objects.filter(resume=resume)
	phone = Phone.objects.filter(resume=resume)
	address = Address.objects.filter(resume=resume)
	skill = Skill.objects.filter(resume=resume)
	certification = Certification.objects.filter(resume=resume)
	education = Education.objects.filter(resume=resume)
	employment = Employment.objects.filter(resume=resume) 
	social = Social.objects.filter(resume=resume)
	project = Project.objects.filter(resume=resume)

	context = {'personal':personal,'about':about,'hobby':hobby,'strength':strength,'weakness':weakness,
	'email':email,'education':education,'phone':phone,'address':address,'skill':skill,'certification':certification,
	'employment':employment,'social':social,'project':project}

	return render(request,'psd.html', context)

@login_required(login_url='registerview')
def gr(request):
	user = request.user
	resume = Resume.objects.filter(user=user).first()
	personal = Personal.objects.filter(resume=resume)
	about = About.objects.filter(resume=resume)
	hobby = Hobby.objects.filter(resume=resume)
	strength = Strength.objects.filter(resume=resume)
	weakness = Weakness.objects.filter(resume=resume)
	email = Email.objects.filter(resume=resume)
	phone = Phone.objects.filter(resume=resume)
	address = Address.objects.filter(resume=resume)
	skill = Skill.objects.filter(resume=resume)
	certification = Certification.objects.filter(resume=resume)
	education = Education.objects.filter(resume=resume)
	employment = Employment.objects.filter(resume=resume) 
	social = Social.objects.filter(resume=resume)
	project = Project.objects.filter(resume=resume)

	context = {'personal':personal,'about':about,'hobby':hobby,'strength':strength,'weakness':weakness,
	'email':email,'education':education,'phone':phone,'address':address,'skill':skill,'certification':certification,
	'employment':employment,'social':social,'project':project}

	return render(request,'psd.html', context)

@login_required(login_url='registerview')
def resumebegin(request):
	user = request.user
	if request.method == "POST":
		resume_name = request.POST.get('resume_name')
		

		resume = Resume.objects.create(user=user,name=resume_name)
		resume.save()

		return render(request,'add_information.html',{'resume_name':resume_name})
	else:
		return render(request,'resumebegin.html')

	return render(request,'resumebegin.html')

@login_required(login_url='registerview')
def oldresumeadd(request):
	user = request.user
	if request.method == "POST":
		resume_name = request.POST.get('resume_name')
		

		resume = Resume.objects.get(user=user,name=resume_name)
		if resume is not None:
			return render(request,'add_information.html',{'resume_name':resume_name})
		else:
			return redirect('resumebegin')
	else:
		return render(request,'resumebegin.html')

	return render(request,'resumebegin.html')

@login_required(login_url='registerview')
def addpers(request):
	user = request.user
	if request.method == "POST" and request.FILES["image"]:
		resume_name = request.POST['resume_name']
		name = request.POST['name']
		occupation = request.POST['occupation']
		objective = request.POST['objective']
		image = request.FILES['image']
		nationality = request.POST['nationality']

		resume = Resume.objects.get(user=user,name=resume_name)


		personal = Personal.objects.create(resume=resume,name=name,occupation=occupation,objective=objective,
			image=image, nationality=nationality)

		personal.save()
		return render(request,'add_information.html',{'resume_name':resume_name})
	else:
		return render(request,'add_information.html',{'resume_name':resume_name})

	return render(request,'add_information.html',{'resume_name':resume_name})




@login_required(login_url='registerview')
def addabout(request):
	user = request.user
	if request.method == "POST":
		resume_name = request.POST['resume_name'] 
		aboutme = request.POST['aboutme']

		resume = Resume.objects.get(user=user,name=resume_name)

		abo = About.objects.create(resume=resume,aboutme=aboutme)
		abo.save()

		return render(request,'add_information.html',{'resume_name':resume_name})
	else:
		return render(request,'add_information.html',{'resume_name':resume_name})

	return render(request,'add_information.html',{'resume_name':resume_name})


@login_required(login_url='registerview')
def addhobby(request):
	user = request.user
	if request.method == "POST":
		resume_name = request.POST['resume_name'] 
		name = request.POST['name']

		resume = Resume.objects.get(user=user,name=resume_name)

		hobby = Hobby.objects.create(resume=resume,name=name)
		hobby.save()

		return render(request,'add_information.html',{'resume_name':resume_name})
	else:
		return render(request,'add_information.html',{'resume_name':resume_name})

	return render(request,'add_information.html',{'resume_name':resume_name})


@login_required(login_url='registerview')
def addweak(request):
	user = request.user
	if request.method == "POST":
		resume_name = request.POST['resume_name'] 
		point = request.POST['point']

		resume = Resume.objects.get(user=user,name=resume_name)

		weak = Weakness.objects.create(resume=resume,point=point)
		weak.save()

		return render(request,'add_information.html',{'resume_name':resume_name})
	else:
		return render(request,'add_information.html',{'resume_name':resume_name})

	return render(request,'add_information.html',{'resume_name':resume_name})


@login_required(login_url='registerview')
def addstren(request):
	user = request.user
	if request.method == "POST":
		resume_name = request.POST['resume_name'] 
		point = request.POST['point']

		resume = Resume.objects.get(user=user,name=resume_name)

		stren = Strength.objects.create(resume=resume,point=point)
		stren.save()

		return render(request,'add_information.html',{'resume_name':resume_name})
	else:
		return render(request,'add_information.html',{'resume_name':resume_name})

	return render(request,'add_information.html',{'resume_name':resume_name})






@login_required(login_url='registerview')
def addphone(request):
	user = request.user
	if request.method == "POST":
		resume_name = request.POST['resume_name'] 
		number = request.POST['number']

		resume = Resume.objects.get(user=user,name=resume_name)

		phn = Phone.objects.create(resume=resume,number=number)
		phn.save()

		return render(request,'add_information.html',{'resume_name':resume_name})
	else:
		return render(request,'add_information.html',{'resume_name':resume_name})

	return render(request,'add_information.html',{'resume_name':resume_name})

@login_required(login_url='registerview')
def addmail(request):
	user = request.user
	if request.method == "POST":
		resume_name = request.POST['resume_name'] 
		mail = request.POST['mail']

		resume = Resume.objects.get(user=user,name=resume_name)

		ema = Email.objects.create(resume=resume,mail=mail)
		ema.save()

		return render(request,'add_information.html',{'resume_name':resume_name})
	else:
		return render(request,'add_information.html',{'resume_name':resume_name})

	return render(request,'add_information.html',{'resume_name':resume_name})

		

@login_required(login_url='registerview')
def addaddress(request):
	user = request.user
	if request.method == "POST":
		resume_name = request.POST['resume_name'] 
		house_no = request.POST['house_no'] 
		street = request.POST['street']
		landmark = request.POST['landmark']
		city = request.POST['city']
		district = request.POST['district']
		state = request.POST['state']
		country = request.POST['country']
		pin = request.POST['pin']

		resume = Resume.objects.get(user=user,name=resume_name)

		ads = Address.objects.create(resume=resume,house_no=house_no,street=street,landmark=landmark,
			city=city,district=district,state=state,country=country,pin=pin)
		ads.save()

		return render(request,'add_information.html',{'resume_name':resume_name})
	else:
		return render(request,'add_information.html',{'resume_name':resume_name})

	return render(request,'add_information.html',{'resume_name':resume_name})




@login_required(login_url='registerview')
def addcert(request):
	user = request.user
	if request.method == "POST":
		resume_name = request.POST['resume_name'] 
		name = request.POST['name'] 
		mode = request.POST['mode']
		link = request.POST['link']

		resume = Resume.objects.get(user=user,name=resume_name)

		soc = Certification.objects.create(resume=resume,name=name,mode=mode,link=link)
		soc.save()

		return render(request,'add_information.html',{'resume_name':resume_name})
	else:
		return render(request,'add_information.html',{'resume_name':resume_name})

	return render(request,'add_information.html',{'resume_name':resume_name})



@login_required(login_url='registerview')
def addskill(request):
	user = request.user
	if request.method == "POST":
		resume_name = request.POST['resume_name'] 
		skilltype = request.POST['skilltype'] 
		name = request.POST['name']

		resume = Resume.objects.get(user=user,name=resume_name)

		ski = Skill.objects.create(resume=resume,skilltype=skilltype,name=name)
		ski.save()

		return render(request,'add_information.html',{'resume_name':resume_name})
	else:
		return render(request,'add_information.html',{'resume_name':resume_name})

	return render(request,'add_information.html',{'resume_name':resume_name})


@login_required(login_url='registerview')
def addedu(request):
	user = request.user
	if request.method == "POST":
		resume_name = request.POST['resume_name'] 
		edu_type = request.POST['edu_type'] 
		institution = request.POST['institution']
		affiliation = request.POST['affiliation']
		start = int(request.POST['start'])
		end = int(request.POST['end'])
		stream = request.POST['stream']
		marks = str(request.POST['marks'])

		resume = Resume.objects.get(user=user,name=resume_name)

		edu = Education.objects.create(resume=resume,edu_type=edu_type,institution=institution,
			affiliation=affiliation,start=start,end=end,stream=stream,marks=marks)
		edu.save()

		return render(request,'add_information.html',{'resume_name':resume_name})
	else:
		return render(request,'add_information.html',{'resume_name':resume_name})

	return render(request,'add_information.html',{'resume_name':resume_name})




@login_required(login_url='registerview')
def addsocial(request):
	user = request.user
	if request.method == "POST":
		resume_name = request.POST['resume_name'] 
		platform = request.POST['platform'] 
		name = request.POST['name']
		link = request.POST['link']

		resume = Resume.objects.get(user=user,name=resume_name)

		soc = Social.objects.create(resume=resume,platform=platform,name=name,link=link)
		soc.save()

		return render(request,'add_information.html',{'resume_name':resume_name})
	else:
		return render(request,'add_information.html',{'resume_name':resume_name})

	return render(request,'add_information.html',{'resume_name':resume_name})




@login_required(login_url='registerview')
def addproject(request):
	user = request.user
	if request.method == "POST":
		resume_name = request.POST['resume_name'] 
		title = request.POST['title'] 
		desc = request.POST['desc']
		link = request.POST['link']

		resume = Resume.objects.get(user=user,name=resume_name)

		pro = Project.objects.create(resume=resume,title=title,desc=desc,link=link)
		pro.save()

		return render(request,'add_information.html',{'resume_name':resume_name})
	else:
		return render(request,'add_information.html',{'resume_name':resume_name})

	return render(request,'add_information.html',{'resume_name':resume_name})



	

@login_required(login_url='registerview')
def addjob(request):
	user = request.user
	if request.method == "POST":
		resume_name = request.POST['resume_name'] 
		employer = request.POST['employer']
		jobtitle = request.POST['jobtitle']
		jobdesc = request.POST['jobdesc']
		jobcity = request.POST['jobcity']
		jobstate = request.POST['jobstate']
		jobstart = request.POST['jobstart']
		jobend = request.POST['jobend']

		resume = Resume.objects.get(user=user,name=resume_name)

		emp = Employment.objects.create(resume=resume,employer=employer,jobtitle=jobtitle,jobdesc=jobdesc,
			jobcity=jobcity,jobstate=jobstate,jobstart=jobstart,jobend=jobend
			)


		emp.save()

		return render(request,'add_information.html',{'resume_name':resume_name})


	else:

		return render(request,'add_information.html',{'resume_name':resume_name})

	return render(request,'add_information.html',{'resume_name':resume_name})



