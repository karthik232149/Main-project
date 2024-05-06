import base64
import datetime

import subprocess
from time import strptime

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from .models import *
# Create your views here.
def login(request):
    return render(request,"loginindex.html")

def login_post(request):
    username=request.POST['textfield']
    password=request.POST['textfield2']
    if Login.objects.filter(Username=username,Password=password).exists():
        a=Login.objects.get(Username=username,Password=password)
        request.session['lid']=a.id
        request.session['log']="lin"
        if a.Type=='Admin':
            # return render(request,'Admin/home.html')
            return render(request,'Admin/homeindex.html')
        elif a.Type=="trainer":
            return render(request,"trainer/homeindex.html")

        elif a.Type=='user':
            return render(request,"user/welcomepage.html")

        else:
            return HttpResponse("<script>alert('user not found');window.location='/Aiyoga/login/'</script>")
    else:
        return HttpResponse("<script>alert('user not found');window.location='/Aiyoga/login/'</script>")


def userhome(request):
    return render(request,"user/welcomepage.html")

def yogapose(request):
    program = "C:\\Program Files\\Python311\\python.exe C:\\Users\\user\\OneDrive\\Desktop\\Setup\\yoga-main\\yoga-main\\inference.py"

    process = subprocess.Popen(program)

    code = process.wait()

    print(code)

    return  redirect('/Aiyoga/userhome/')

def admin_home(request):
    if request.session['log']=="lin":
        return render(request,"admin/homeindex.html")
    else:
        return HttpResponse("<script>alert('Already logged out');window.location='/Aiyoga/Logout/'</script>")

def trainer_home(request):
    if request.session['log']=="lin":
        return render(request,"trainer/homeindex.html")
    else:
        return HttpResponse("<script>alert('Already logged out');window.location='/Aiyoga/Logout/'</script>")


def addtrainer(request):
    return render(request,'trainer/signupindex.html')


def add_trainer_post(request):
        name=request.POST['textfield']
        email=request.POST['textfield2']
        phone=request.POST['textfield3']
        place=request.POST['textfield4']
        post=request.POST['textfield5']
        pin=request.POST['textfield6']
        dob=request.POST['textfield7']
        Experience=request.POST['textfield8']
        password=request.POST['Password']
        cpass=request.POST['Password2']
        gender=request.POST['RadioGroup1']
        photo=request.FILES['file']


        if password==cpass:
            from datetime import datetime
            date=datetime.now().strftime('%Y%m%d-%H%M%S')+'.jpg'
            fs=FileSystemStorage()
            fs.save(date,photo)
            path=fs.url(date)


            res=Trainer.objects.filter(EmaiL=email)
            if res.exists():
                return HttpResponse(
                    "<script>alert('Already Registred');window.location='/Aiyoga/login/'</script>")
            else:
                b = Login()
                b.Username = email
                b.Password = phone
                b.Type = 'pending'
                b.save()

                a=Trainer()
                a.Name=name
                a.EmaiL=email
                a.Post=post
                a.Pin=pin
                a.Dob=dob
                a.PLACE=place
                a.Experience=Experience
                a.Phone=phone
                a.Gender=gender
                a.Photo=path
                a.LOGIN_id=b.id
                a.save()

            return HttpResponse("<script>alert('Registration successfully');window.location='/Aiyoga/login/'</script>")

        else:
            return HttpResponse("<script>alert('Password missmatch');window.location='/Aiyoga/addtrainer/'</script>")

def edittrainer(request,id):
    if request.session['log'] == "lin":
        e=Trainer.objects.get(id=id)
        return render(request,'Admin/Edit trainer.html',{'data':e})
    else:
        return HttpResponse("<script>alert('Already logged out');window.location='/Aiyoga/Logout/'</script>")


def edit_trainer_post(request):
    if request.session['log']  == "lin":
        name=request.POST['textfield']
        email=request.POST['textfield2']
        phone=request.POST['textfield3']
        Experience=request.POST['textfield8']
        place=request.POST['textfield4']
        post=request.POST['textfield7']
        pin=request.POST['textfield5']
        Dob=request.POST['textfield6']
        gender=request.POST['RadioGroup1']
        id=request._post['id']
        d=Trainer.objects.get(id=id)
        res = Trainer.objects.get(id=id).EmaiL
        if res==email:
            if 'photo' in request.FILES:
                photo = request.FILES['photo']
                from datetime import datetime
                date = datetime.now().strftime('%Y%m%d-%H%M%S') + '.jpg'
                fs = FileSystemStorage()
                fs.save(date, photo)
                path = fs.url(date)
                d.Photo = path
                d.save()

            d.Name = name
            d.EmaiL = email
            d.Phone = phone
            d.Experience = Experience
            d.PLACE = place
            d.Pin = pin
            d.Post = post
            d.Dob = Dob
            d.Gender = gender
            d.save()

            obj = Login.objects.get(id=d.LOGIN_id)
            obj.Username = email
            obj.save()
            return HttpResponse("<script>alert('Edited successfully');window.location='/Aiyoga/view_trainer/'</script>")
        elif Trainer.objects.filter(EmaiL=email).exists():
            return HttpResponse("<script>alert('Already Registred');window.location='/Aiyoga/view_trainer/'</script>")
        else:
            if 'photo' in request.FILES:
                photo = request.FILES['photo']
                from datetime import datetime
                date = datetime.now().strftime('%Y%m%d-%H%M%S') + '.jpg'
                fs = FileSystemStorage()
                fs.save(date, photo)
                path = fs.url(date)
                d.Photo = path
                d.save()

            d.Name = name
            d.EmaiL = email
            d.Phone = phone
            d.Experience = Experience
            d.PLACE = place
            d.Pin = pin
            d.Post = post
            d.Dob = Dob
            d.Gender = gender
            d.save()

            obj = Login.objects.get(id=d.LOGIN_id)
            obj.Username = email
            obj.save()
            return HttpResponse("<script>alert('Edited successfully');window.location='/Aiyoga/view_trainer/'</script>")

    else:
        return HttpResponse("<script>alert('Already logged out');window.location='/Aiyoga/Logout/'</script>")


def view_trainer(request):
    if request.session['log'] == "lin":
        c=Trainer.objects.filter(Status='pending').order_by('-id')
        return render(request,"Admin/view trainer.html",{'data':c})
    else:
        return HttpResponse("<script>alert('Already logged out');window.location='/Aiyoga/Logout/'</script>")


def view_approved_trainer(request):
    if request.session['log'] == "lin":
        c=Trainer.objects.filter(Status='approved').order_by('-id')
        return render(request,"Admin/view approved trainer.html",{'data':c})
    else:
        return HttpResponse("<script>alert('Already logged out');window.location='/Aiyoga/Logout/'</script>")

def view_approved_trainer_post(request):
    if request.session['log'] == "lin":
        search=request.POST['textfield']
        c=Trainer.objects.filter(Status='approved',Name__icontains=search).order_by('-id')
        return render(request,"Admin/view approved trainer.html",{'data':c})
    else:
        return HttpResponse("<script>alert('Already logged out');window.location='/Aiyoga/Logout/'</script>")


def view_rejected_trainer(request):
    if request.session['log'] == "lin":
        c=Trainer.objects.filter(Status='rejected').order_by('-id')
        return render(request,"Admin/view rejected trainer.html",{'data':c})
    else:
        return HttpResponse("<script>alert('Already logged out');window.location='/Aiyoga/Logout/'</script>")


def view_rejected_trainer_post(request):
    if request.session['log'] == "lin":
        search=request.POST['textfield']
        c=Trainer.objects.filter(Status='rejected',Name__icontains=search).order_by('-id')
        return render(request,"Admin/view rejected trainer.html",{'data':c})
    else:
        return HttpResponse("<script>alert('Already logged out');window.location='/Aiyoga/Logout/'</script>")


def approve_triner(request,id):
    res=Trainer.objects.filter(LOGIN=id).update(Status='approved')
    rs=Login.objects.filter(id=id).update(Type='trainer')
    return HttpResponse("<script>alert('Approved');window.location='/Aiyoga/view_trainer/'</script>")

def approve_triner_new(request,id):
    res=Trainer.objects.filter(LOGIN=id).update(Status='approved')
    rs=Login.objects.filter(id=id).update(Type='trainer')
    return HttpResponse("<script>alert('Approved');window.location='/Aiyoga/view_approved_trainer/'</script>")

def reject_triner_new(request,id):
    res=Trainer.objects.filter(LOGIN=id).update(Status='rejected')
    rs=Login.objects.filter(id=id).update(Type='rejected')
    return HttpResponse("<script>alert('Rejected');window.location='/Aiyoga/view_rejected_trainer/'</script>")


def reject_triner(request,id):
    res=Trainer.objects.filter(LOGIN=id).update(Status='rejected')
    rs=Login.objects.fiter(id=id).update(Type='rejected')
    return HttpResponse("<script>alert('Rejected');window.location='/Aiyoga/view_trainer/'</script>")

def deleted_trainer(request):
    if request.session['log'] == "lin":
        c=Trainer.objects.filter(Status='deleted')
        return render(request,"Admin/deleted trainer.html",{'data':c})
    else:
        return HttpResponse("<script>alert('Already logged out');window.location='/Aiyoga/Logout/'</script>")

def deleted_trainer_Post(request):
    if request.session['log'] == "lin":
        search = request.POST['textfield']
        c=Trainer.objects.filter(Status='deleted',Name__icontains=search).order_by('-id')
        return render(request,"Admin/deleted trainer.html",{'data':c})
    else:
        return HttpResponse("<script>alert('Already logged out');window.location='/Aiyoga/Logout/'</script>")


def viewtrainer_post(request):
    if request.session['log'] == "lin":
        search=request.POST['textfield']
        c = Trainer.objects.filter(Status='pending',Name__icontains=search)
        return render(request,'Admin/view trainer.html',{'data':c})
    else:
        return HttpResponse("<script>alert('Already logged out');window.location='/Aiyoga/Logout/'</script>")





def delete_trainer(request,id):
    if request.session['log'] == "lin":
        # rea=Trainer.objects.filter(id=id).delete()
        rea=Trainer.objects.filter(id=id).update(Status='deleted')
        return HttpResponse("<script>alert('delete successfully');window.location='/Aiyoga/view_trainer/'</script>")
    else:
        return HttpResponse("<script>alert('Already logged out');window.location='/Aiyoga/Logout/'</script>")

def Viewcomplaints(request):
    a = Complaint.objects.all()
    return render(request, "Admin/View complaint.html", {'data': a})




def Viewcomplaintspost(request):
    fdate=request.POST['textfield']
    tdate=request.POST['textfield2']
    a = Complaint.objects.filter(Date__range=[fdate,tdate])
    return render(request, "Admin/View complaint.html", {'data': a})


def Sendreply(request, id):
    return render(request, 'admin/send reply.html', {'id': id})

def sendreplypost(request):
    id = request.POST['id']
    reply = request.POST['textarea']
    obj = Complaint.objects.filter(id=id).update(reply=reply, Status='replied')
    return HttpResponse("<script>alert('send');window.location='/Aiyoga/Viewcomplaints/'</script>")


def Viewfeedback(request):
    a = Feedback.objects.all()
    return render(request, "Admin/View feedback.html", {'data': a})

def Viewfeedbackspost(request):
    fdate=request.POST['textfield']
    tdate=request.POST['textfield2']
    a = Feedback.objects.filter(Date__range=[fdate,tdate])
    return render(request, "Admin/View feedback.html", {'data': a})

#################################### trainer ######################


def Trainer_view_profile(request):
    if request.session['log'] == "lin":
        res=Trainer.objects.get(LOGIN__id=request.session['lid'])
        return render(request,"trainer/viewprofile.html",{"data":res})
    else:
        return HttpResponse("<script>alert('Already logged out');window.location='/Aiyoga/Logout/'</script>")

@csrf_exempt
def reg(request):
    email  = request.POST['textfield2']
    print(email)
    data = {
        'is_taken': str(Login.objects.filter(Username__iexact=email).exists())
    }
    # if data['is_taken']:
    #     data['is_taken']="True"
    print(data['is_taken'], 'dataaaa')
    return JsonResponse({"status":str(data['is_taken']),"data":data})
def Trainer_edit_profile(request):
    a=Trainer.objects.get(LOGIN_id=request.session['lid'])
    return render(request,'trainer/editprofile.html',{'data':a})

def Trainer_edit_profile_post(request):
    Name=request.POST['textfield']
    Email=request.POST['textfield2']
    Phone=request.POST['textfield3']
    Experience=request.POST['textfield8']
    Post=request.POST['textfield4']
    Place=request.POST['textfield7']
    Pin=request.POST['textfield5']
    Gender=request.POST['RadioGroup1']
    Dob=request.POST['textfield6']
    # Photo=request.POST['Photo']
    # id=request.POST['lid']
    # if
    a=Trainer.objects.get(LOGIN_id=request.session['lid'])
    # if a == Email:
    if 'photo' in request.FILES:
        photo = request.FILES['photo']
        from datetime import datetime
        date = datetime.now().strftime('%Y%m%d-%H%M%S') + '.jpg'
        fs = FileSystemStorage()
        fs.save(date, photo)
        path = fs.url(date)
        a.Photo = path
        a.save()
    a.Name=Name
    a.EmaiL=Email
    a.Phone=Phone
    a.Experience=Experience
    a.Post=Post
    a.Place=Place
    a.Pin=Pin
    a.Gender=Gender
    a.Dob=Dob
    a.save()
    # b=Login.objects.filter(id=request.session['lid']).update(Username=Email)
    return HttpResponse("<script>alert('Edited successfully');window.location='/Aiyoga/Trainer_view_profile/'</script>")
    # elif Trainer.objects.filter(EmaiL=Email).exists():
    #     return HttpResponse("<script>alert('Email Already Registred');window.location='/Aiyoga/Trainer_view_profile/'</script>")
    # else:
    #     return HttpResponse("<script>alert('Updated...');window.location='/Aiyoga/Trainer_view_profile/'</script>")




def Logout(request):
    request.session['log']=""
    return render(request,"loginindex.html")

def Addtips(request):
    return render(request,'trainer/Addtip.html')


def Addtips_post(request):
    Title=request.POST['textfield']
    Description=request.POST['textfield2']
    a=Tips()
    a.Title=Title
    a.Description=Description
    a.Date=datetime.date.today()
    a.TRAINER=Trainer.objects.get(LOGIN_id=request.session['lid'])
    a.save()
    return HttpResponse("<script>alert('Tip added successfully');window.location='/Aiyoga/trainer_Addtips/'</script>")

def Deletetips(request,id):
    a=Tips.objects.filter(id=id).delete()
    return HttpResponse("<script>alert('Tip deleted successfully');window.location='/Aiyoga/trainer_Viewtips/'</script>")

def Edittips(request,id):
    a=Tips.objects.get(id=id)
    return render(request,'trainer/Edittip.html',{'data':a})

def Edittips_post(request):
    id=request.POST['id']
    Title=request.POST['textfield']
    Description=request.POST['textfield2']
    a=Tips.objects.get(id=id)
    a.Title=Title
    a.Description=Description
    a.Date=datetime.date.today()
    a.save()
    return HttpResponse("<script>alert('Tips edited successfully');window.location='/Aiyoga/trainer_Viewtips/'</script>")

def Viewtips(request):
    t=Tips.objects.filter(TRAINER__LOGIN_id=request.session['lid']).order_by('-id')
    print(t,"tttttt")
    return render(request,'trainer/view tips.html',{'data':t})


def Viewtips_post(request):
    d=request.POST['textfield']
    t = Tips.objects.filter(TRAINER__LOGIN_id=request.session['lid'], Title__icontains=d)
    return render(request, 'trainer/view tips.html',{'data':t})

def email_exist(request):
    email = request.POST['email']

    status = Trainer.objects.filter(email_address = email).exists()
    return JsonResponse({'status':status})


def Viewrequest(request):
    res=Request.objects.filter(Status='pending')
    return render(request,'trainer/viewrequests.html',{'data':res})


def viewrequest_post(request):
    f=request.POST['textfield']
    t=request.POST['textfield2']
    res=Request.objects.filter(Status='pending',Date__range=[f,t])
    return render(request,'trainer/viewrequests.html',{'data':res})




def approvereq(request,id):
    res=Request.objects.filter(pk=id).update(Status='approve')
    return HttpResponse(
        "<script>alert('request approved successfully');window.location='/Aiyoga/viewrequests/'</script>")



def rejectreq(request,id):
    res=Request.objects.filter(pk=id).update(Status='reject')
    return HttpResponse(
        "<script>alert('request rejected successfully');window.location='/Aiyoga/viewrequests/'</script>")

def Viewapprovedrequest(request):
    res=Request.objects.filter(Status='approve')
    return render(request,'trainer/viewapproverequests.html',{'data':res})

def viewapprovedrequest_post(request):
    f = request.POST['textfield']
    t = request.POST['textfield2']
    res = Request.objects.filter(Status='approve', Date__range=[f, t])
    return render(request, 'trainer/viewapproverequests.html', {'data': res})


def Viewrejectedrequest(request):
    res=Request.objects.filter(Status='reject')
    return render(request,'trainer/viewrejectrequests.html',{'data':res})

def viewrejectedrequest_post(request):
    f = request.POST['textfield']
    t = request.POST['textfield2']
    res = Request.objects.filter(Status='reject', Date__range=[f, t])
    return render(request,'trainer/viewrejectrequests.html',{'data':res})


def Trainer_Adddietchart(request):
    return render(request, 'trainer/Adddietchart.html')

def Adddietchart_post(request):
    BMI = request.POST['textfield26']
    PREGNANCY = request.POST['textfield25']
    ARTHRITIS = request.POST['textfield24']
    ALLERGIES=request.POST['textfield23']
    DEPRESSION=request.POST['textfield22']
    LIVERPROBLEM=request.POST['textfield21']
    KIDNEYPROBLEM=request.POST['textfield20']
    BONEJOINT=request.POST['textfield19']
    STROKE=request.POST['textfield18']
    CANCER=request.POST['textfield17']
    HEARTPROBLEM=request.POST['textfield16']
    ASTHMA=request.POST['textfield15']
    SMOKING=request.POST['textfield14']
    DRUGUSE=request.POST['textfield13']
    ALCOHOLUSE=request.POST['textfield12']
    CHOLESTROL=request.POST['textfield11']
    DIABETES=request.POST['textfield10']
    BLOODPRESSURE=request.POST['textfield9']
    OBESITY=request.POST['textfield8']
    GENDER=request.POST['textfield7']
    AGE=request.POST['textfield6']
    WEIGHT=request.POST['textfield5']
    HEIGHT=request.POST['textfield4']
    HEADACHES=request.POST['textfield27']
    TIME=request.POST['textfield28']
    MENU=request.POST['textfield']
    QUANTITY=request.POST['textfield2']
    a=Diet_chart()
    a.menu=MENU
    a.quantity=QUANTITY
    a.Date = datetime.date.today()
    a.Time=TIME
    a.Height=HEIGHT
    a.Weight=WEIGHT
    a.Age=AGE
    a.Gender=GENDER
    a.Obesity=OBESITY
    a.Blood_pressure=BLOODPRESSURE
    a.Diabetes=DIABETES
    a.Cholesterol=CHOLESTROL
    a.Alcohol_use=ALCOHOLUSE
    a.Drug_use=DRUGUSE
    a.Smoking=SMOKING
    a.Asthma=ASTHMA
    a.Heart_problems=HEARTPROBLEM
    a.Cancer=CANCER
    a.Stroke=STROKE
    a.Bone_joint=BONEJOINT
    a.Kidney_problem=KIDNEYPROBLEM
    a.Liver_problems=LIVERPROBLEM
    a.Depression=DEPRESSION
    a.Allergies=ALLERGIES
    a.Arthritis=ARTHRITIS
    a.Pregnancy=PREGNANCY
    a.Headaches=HEADACHES
    a.Bmi=BMI
    a.TRAINER=Trainer.objects.get(LOGIN_id=request.session['lid'])
    a.save()
    return HttpResponse("<script>alert('Diet chart  added successfully');window.location='/Aiyoga/Trainer_Adddietchart/'</script>")
def Trainer_Deletedietchart(request,id):
    a=Diet_chart.objects.filter(id=id).delete()
    return HttpResponse("<script>alert('Diet chart deleted successfully');window.location='/Aiyoga/Trainer_Viewdietchart/'</script>")
def Trainer_Editdietchart(request,id):
    a=Diet_chart.objects.get(id=id)
    return render(request,'trainer/Editdietchart.html',{'data':a})


def Editdietchart_post(request):
    BMI = request.POST['textfield26']
    PREGNANCY = request.POST['textfield25']
    ARTHRITIS = request.POST['textfield24']
    ALLERGIES = request.POST['textfield23']
    DEPRESSION = request.POST['textfield22']
    LIVERPROBLEM = request.POST['textfield21']
    KIDNEYPROBLEM = request.POST['textfield20']
    BONEJOINT = request.POST['textfield19']
    STROKE = request.POST['textfield18']
    CANCER = request.POST['textfield17']
    HEARTPROBLEM = request.POST['textfield16']
    ASTHMA = request.POST['textfield15']
    SMOKING = request.POST['textfield14']
    DRUGUSE = request.POST['textfield13']
    ALCOHOLUSE = request.POST['textfield12']
    CHOLESTROL = request.POST['textfield11']
    DIABETES = request.POST['textfield10']
    BLOODPRESSURE = request.POST['textfield9']
    OBESITY = request.POST['textfield8']
    GENDER = request.POST['textfield7']
    AGE = request.POST['textfield6']
    WEIGHT = request.POST['textfield5']
    HEIGHT = request.POST['textfield4']
    HEADACHES = request.POST['textfield27']
    id=request.POST['id']
    MENU=request.POST['textfield']
    QUNTITY=request.POST['textfield2']
    TIME=request.POST['textfield28']
    a=Diet_chart.objects.get(id=id)
    a.menu = MENU
    a.quantity = QUNTITY
    a.Date = datetime.date.today()
    a.Height = HEIGHT
    a.Weight = WEIGHT
    a.Age = AGE
    a.Gender = GENDER
    a.Obesity = OBESITY
    a.Blood_pressure = BLOODPRESSURE
    a.Diabetes = DIABETES
    a.Cholesterol = CHOLESTROL
    a.Alcohol_use = ALCOHOLUSE
    a.Drug_use = DRUGUSE
    a.Smoking = SMOKING
    a.Asthma = ASTHMA
    a.Heart_problems = HEARTPROBLEM
    a.Cancer = CANCER
    a.Stroke = STROKE
    a.Bone_joint = BONEJOINT
    a.Kidney_problem = KIDNEYPROBLEM
    a.Liver_problems = LIVERPROBLEM
    a.Depression = DEPRESSION
    a.Allergies = ALLERGIES
    a.Arthritis = ARTHRITIS
    a.Pregnancy = PREGNANCY
    a.Headaches = HEADACHES
    a.Bmi = BMI
    a.Time=TIME
    a.save()
    return HttpResponse("<script>alert('Diet chart edited successfully');window.location='/Aiyoga/Trainer_Viewdietchart/'</script>")

def Trainer_Viewdietchart(request):
    t=Diet_chart.objects.filter(TRAINER__LOGIN_id=request.session['lid'])
    print(t)
    return render(request, 'trainer/view dietchart.html', {'data':t})


def Viewdietchart_post(request):
    d=request.POST['textfield']
    t = Diet_chart.objects.filter(TRAINER__LOGIN_id=request.session['lid'],menu__icontains=d)
    return render(request, 'trainer/view dietchart.html', {'data':t})



def Trainer_add_diet_profile(request):
    return render(request, 'trainer/Adddietchart.html')



def Trainer_add_diet_profile_post(request):
    lid=request.POST['lid']
    weight=request.POST['weight']
    Height=request.POST['Height']
    Age=request.POST['age']
    Gender=request.POST['Gender']
    Obesity=request.POST['Obesity']
    Blood_pressure=request.POST['Blood_pressure']
    Diabetes=request.POST['Diabetes']
    Cholesterol=request.POST['Cholesterol']
    Alcohol_use=request.POST['Alcohol_use']
    Drug_use=request.POST['Drug_use']
    Smoking=request.POST['Smoking']
    Headaches=request.POST['Headaches']
    Asthma=request.POST['Asthma']
    Heart_problems=request.POST['Heart_problems']
    Cancer=request.POST['Cancer']
    Stroke=request.POST['Stroke']
    Bone_joint=request.POST['Bone_joint']
    Kidney_problem=request.POST['Kidney_problem']
    Liver_problems=request.POST['Liver_problems']
    Depression=request.POST['Depression']
    Allergies=request.POST['Allergies']
    Arthritis=request.POST['Arthritis']
    Pregnancy=request.POST['Pregnancy']

    the_height = float(Height)
    the_weight = float(weight)

    the_BMI = the_weight / (the_height / 100) ** 2

    print("Your Body Mass Index is",str(the_BMI)[:5])

    if the_BMI <= 18.5:
        bmi="Oops! You are underweight."+str(the_BMI)[:5]
    elif the_BMI <= 24.9:
        bmi="Awesome! You are healthy."+str(the_BMI)[:5]
    elif the_BMI <= 29.9:
        bmi="Eee! You are over weight."+str(the_BMI)[:5]
    else:
        bmi="Seesh! You are obese."+str(the_BMI)[:5]

    if Health_profile.objects.filter(USER__LOGIN_id=lid).exists():
        u = Health_profile.objects.get(USER__LOGIN_id =lid)
        u.Height = Height
        u.Weight = weight
        u.Age = Age
        u.Gender = Gender
        u.Obesity = Obesity
        u.Blood_pressure = Blood_pressure
        u.Diabetes = Diabetes
        u.Cholesterol = Cholesterol
        u.Alcohol_use = Alcohol_use
        u.Drug_use = Drug_use
        u.Smoking = Smoking
        u.Headaches = Headaches
        u.Asthma = Asthma
        u.Heart_problems = Heart_problems
        u.Cancer = Cancer
        u.Stroke = Stroke
        u.Bone_joint = Bone_joint
        u.Kidney_problem = Kidney_problem
        u.Liver_problems = Liver_problems
        u.Depression = Depression
        u.Allergies = Allergies
        u.Arthritis = Arthritis
        u.Pregnancy=Pregnancy
        u.Bmi=bmi
        # u.USER = User.objects.get(LOGIN_id=lid)
        u.save()
        return HttpResponse("<script>alert('Diet profile edited successfully');window.location='/Aiyoga/Trainer_add_diet_profile/'</script>")

    u=Health_profile()
    u.Height=Height
    u.Weight=weight
    u.Age=Age
    u.Gender=Gender
    u.Obesity=Obesity
    u.Blood_pressure=Blood_pressure
    u.Diabetes=Diabetes
    u.Cholesterol=Cholesterol
    u.Alcohol_use=Alcohol_use
    u.Drug_use=Drug_use
    u.Smoking=Smoking
    u.Headaches=Headaches
    u.Asthma=Asthma
    u.Heart_problems=Heart_problems
    u.Cancer=Cancer
    u.Stroke=Stroke
    u.Bone_joint=Bone_joint
    u.Kidney_problem=Kidney_problem
    u.Liver_problems=Liver_problems
    u.Depression=Depression
    u.Allergies=Allergies
    u.Arthritis=Arthritis
    u.Pregnancy=Pregnancy
    u.Bmi=bmi
    u.USER=User.objects.get(LOGIN_id=lid)
    u.save()
    return HttpResponse("<script>alert('Diet profile edited successfully');window.location='/Aiyoga/Trainer_add_diet_profile/'</script>")


def view_user(request):
    a=User.objects.all()
    return render(request,'trainer/view users.html',{'data':a})


def chat1(request, id):
    request.session["userid"] = id
    cid = str(request.session["userid"])
    request.session["new"] = cid
    qry = User.objects.get(LOGIN=cid)

    return render(request, "trainer/Chat.html", {'photo': qry.Photo, 'name': qry.Name, 'toid': cid})


def chat_view(request):
    fromid = request.session["lid"]
    toid = request.session["userid"]
    qry = User.objects.get(LOGIN=request.session["userid"])
    from django.db.models import Q

    res = Chat.objects.filter(Q(FROMID_id=fromid, TOID_id=toid) | Q(FROMID_id=toid, TOID_id=fromid))
    l = []

    for i in res:
        import datetime
        import datetime
        parsed_time = datetime.datetime.strptime(str(i.Time)[:5], '%H:%M')
        formatted_time = parsed_time.strftime('%I:%M %p')
        l.append({"id": i.id, "message": i.message, "to": i.TOID_id, "date": i.Date, "from": i.FROMID_id,'time':str(formatted_time)+' '+str(i.Date)})

    return JsonResponse({'photo': qry.Photo, "data": l, 'name': qry.Name, 'toid': request.session["userid"]})


def chat_send(request, msg):
    lid = request.session["lid"]
    toid = request.session["userid"]
    message = msg

    import datetime
    d = datetime.datetime.now().date()
    chatobt = Chat()
    chatobt.message = message
    chatobt.TOID_id = toid
    chatobt.FROMID_id = lid
    chatobt.Date = d
    chatobt.Time = datetime.datetime.now().strftime("%H:%M:%S")
    chatobt.save()

    return JsonResponse({"status": "ok"})


def User_sendchat(request):
    FROM_id = request.POST['from_id']
    TOID_id = request.POST['to_id']
    print(FROM_id)
    print(TOID_id)
    msg = request.POST['message']

    from  datetime import datetime
    c = Chat()
    c.FROMID_id = FROM_id
    c.TOID_id = TOID_id
    c.message = msg
    c.Date = datetime.now()
    c.Time = datetime.now().strftime("%H:%M:%S")
    c.save()
    return JsonResponse({'status': "ok"})

def User_viewchat(request):
    fromid = request.POST["from_id"]
    toid = request.POST["to_id"]
    # lmid = request.POST["lastmsgid"]
    from django.db.models import Q

    res = Chat.objects.filter(Q(FROMID_id=fromid, TOID_id=toid) | Q(FROMID_id=toid, TOID_id=fromid))
    l = []

    for i in res:
        import datetime
        parsed_time = datetime.datetime.strptime(str(i.Time)[:5],'%H:%M')
        formatted_time = parsed_time.strftime('%I:%M %p')
        l.append({"id": i.id, "msg": i.message, "from": i.FROMID_id, "date": i.Date, "to": i.TOID_id,'time':str(formatted_time)+' '+str(i.Date)})

    return JsonResponse({"status":"ok",'data':l})











        #####################################user##################################################################

def User_login_post(request):
    username=request.POST['username']
    password=request.POST['password']
    if Login.objects.filter(Username=username,Password=password).exists():
        a=Login.objects.get(Username=username,Password=password)
        lid=a.id

        if a.Type=='user':
            # return render(request,'Admin/home.html')
            return JsonResponse({'status':'ok','lid':str(lid)})
        else:
            return JsonResponse({'status': 'no'})
    else:
        return JsonResponse({'status': 'no'})



def User_signup_post(request):
    name=request.POST['name']
    email = request.POST['email']
    phone=request.POST['phone']
    post=request.POST['post']
    pin=request.POST['pin']
    dob=request.POST['dob']
    gender=request.POST['gender']
    photo=request.POST['photo']
    place=request.POST['place']
    password=request.POST['password']
    conpassword=request.POST['conpassword']
    if Login.objects.filter(Username=email).exists():
        return JsonResponse({'status':'no'})
    else:
        l=Login()
        l.Username=email
        l.Password=conpassword
        l.Type='user'
        l.save()

        u=User()
        u.Name=name
        u.EmaiL=email
        u.Phone=phone
        u.Post=post
        u.Pin= pin
        u.Dob=dob
        u.Gender= gender
        dt=datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')+'.jpg'
        from untitled import settings
        a=base64.b64decode(photo)
        open(settings.MEDIA_ROOT+'\\user\\'+dt,'wb').write(a)
        u.Photo= '/media/user/'+dt
        u.PLACE= place
        u.LOGIN=l
        u.save()
        return JsonResponse({'status': 'ok'})

def User_Viewyogatrainers(request):
    s=Trainer.objects.all()
    lid=request.POST['lid']
    # s=Request.objects.filter(USER__LOGIN_id=lid).exclude()
    c=[]
    for i in s:
        c.append({'id':i.id, 'name':i.Name, 'photo':i.Photo,'place':i.PLACE,'phone':i.Phone,'gender':i.Gender})

    return JsonResponse({'status': 'ok','data':c})



# def User_Viewyogatrainers(request):
#     lid = request.POST['lid']
#     requests_for_user = Request.objects.filter(USER__LOGIN_id=lid)
#     trainers = []
#     for request in requests_for_user:
#         trainers.append({
#             'id': request.TRAINER.id,
#             'name': request.TRAINER.Name,
#             'photo': request.TRAINER.Photo,
#             'place': request.TRAINER.PLACE,
#             'phone': request.TRAINER.Phone,
#             'gender': request.TRAINER.Gender
#         })
#     print(trainers,"haiiiiiiiiiiiiiii")
#     return JsonResponse({'status': 'ok', 'data': trainers})




def User_Viewyogatrainersearch(request):
    search=request.POST['place']
    s=Trainer.objects.filter(PLACE__icontains=search)
    c=[]
    for i in s:
        c.append({'id':i.id, 'name':i.Name, 'photo':i.Photo,'place':i.PLACE,'phone':i.Phone,'gender':i.Gender})

    return JsonResponse({'status': 'ok','data':c})




def User_Viewmytrainers(request):
    lid=request.POST['lid']
    s=Request.objects.filter(USER__LOGIN_id=lid,Status='approve')
    c=[]
    for i in s:
        c.append({'id':i.id,'tid':i.TRAINER.LOGIN.id,"taid":i.TRAINER.id, 'name':i.TRAINER.Name, 'photo':i.TRAINER.Photo,'place':i.TRAINER.PLACE,'phone':i.TRAINER.Phone,'gender':i.TRAINER.Gender})

    return JsonResponse({'status': 'ok','data':c})



def User_Viewmyrequeststatus(request):
        lid = request.POST['lid']
        s = Request.objects.filter(USER__LOGIN_id=lid,)
        c = []
        for i in s:
            c.append({'id': i.id, 'name': i.TRAINER.Name, 'photo': i.TRAINER.Photo, 'place': i.TRAINER.PLACE,
                      'phone': i.TRAINER.Phone, 'gender': i.TRAINER.Gender,'Status': i.Status,'date':i.Date})

        return JsonResponse({'status': 'ok', 'data': c})



def user_send_trainer_requests(request):
    lid=request.POST['lid']
    tid = request.POST['tid']
    if Request.objects.filter(USER__LOGIN_id=lid).exists():
        return JsonResponse({'status':'no'})

    l=Request()
    l.TRAINER_id=tid
    l.Date=datetime.date.today()
    l.USER=User.objects.get(LOGIN_id=lid)
    l.Status='Pending'
    l.save()

    return JsonResponse({'status': 'ok'})

def user_viewprofile(request):
    lid=request.POST['lid']
    res=User.objects.get(LOGIN__id=lid)
    print(res.Photo)
    return JsonResponse({"status":"ok","name":res.Name,"dob":res.Dob,"gender":res.Gender,"email":res.EmaiL,"phone":res.Phone,"place":res.PLACE,"post":res.Post,"pin":res.Pin,"photo":res.Photo})


def user_editprofile(request):
    lid=request.POST['lid']
    name=request.POST['name']
    email = request.POST['email']
    phone=request.POST['phone']
    post=request.POST['post']
    pin=request.POST['pin']
    dob=request.POST['dob']
    gender=request.POST['gender']
    photo=request.POST['photo']
    place=request.POST['place']
    # password=request.POST['password']
    # conpassword=request.POST['conpassword']
    # if Login.objects.filter(Username=email).exists():
    #     return JsonResponse({'status':'no'})
    if len(photo)>0:

        u=User.objects.get(LOGIN_id=lid)
        u.Name=name
        u.EmaiL=email
        u.Phone=phone
        u.Post=post
        u.Pin= pin
        u.Dob=dob
        u.Gender= gender

        from datetime import datetime
        dt=datetime.now().strftime('%Y%m%d%H%M%S%f')+'.jpg'
        from untitled import settings
        a=base64.b64decode(photo)
        open(settings.MEDIA_ROOT+'\\user\\'+dt,'wb').write(a)
        u.Photo= '/media/user/'+dt
        u.PLACE= place
        u.save()
        return JsonResponse({'status': 'ok'})
    else:
        u = User.objects.get(LOGIN_id=lid)
        u.Name = name
        u.EmaiL = email
        u.Phone = phone
        u.Post = post
        u.Pin = pin
        u.Dob = dob
        u.Gender = gender
        u.PLACE = place
        u.save()
        return JsonResponse({'status': 'ok'})



def user_edit_diet_profile_Post(request):
    try:
        lid = request.POST['lid']
        weight = float(request.POST['weight'])
        height = float(request.POST['Height'])
        age = int(request.POST['age'])
        gender = request.POST['Gender']
        obesity = request.POST['Obesity']
        blood_pressure = request.POST['Blood_pressure']
        diabetes = request.POST['Diabetes']
        cholesterol = request.POST['Cholesterol']
        alcohol_use = request.POST['Alcohol_use']
        drug_use = request.POST['Drug_use']
        smoking = request.POST['Smoking']
        headaches = request.POST['Headaches']
        asthma = request.POST['Asthma']
        heart_problems = request.POST['Heart_problems']
        cancer = request.POST['Cancer']
        stroke = request.POST['Stroke']
        bone_joint = request.POST['Bone_joint']
        kidney_problem = request.POST['Kidney_problem']
        liver_problems = request.POST['Liver_problems']
        depression = request.POST['Depression']
        allergies = request.POST['Allergies']
        arthritis = request.POST['Arthritis']
        pregnancy = request.POST['Pregnancy']

        bmi = weight / (height / 100) ** 2
        bmi_category = ""

        # if bmi <= 18.5:
        #     bmi_category = "Underweight"
        # elif bmi <= 24.9:
        #     bmi_category = "Normal weight"
        # elif bmi <= 29.9:
        #     bmi_category = "Overweight"
        # else:
        #     bmi_category = "Obese"
        vv=User.objects.get(LOGIN_id=lid).id
        # if Health_profile.objects.filter(USER_id=vv).exists():
        #     health_profile = Health_profile.objects.get(USER_id=vv)
        # else:

        health_profile = Health_profile(USER_id=vv)
        if (Health_profile.objects.filter(USER__LOGIN_id=lid).exists):
            health_profile = Health_profile.objects.get(USER__LOGIN_id=lid)



        health_profile.Height = height
        health_profile.Weight = weight
        health_profile.Age = age
        health_profile.Gender = gender
        health_profile.Obesity = obesity
        health_profile.Blood_pressure = blood_pressure
        health_profile.Diabetes = diabetes
        health_profile.Cholesterol = cholesterol
        health_profile.Alcohol_use = alcohol_use
        health_profile.Drug_use = drug_use
        health_profile.Smoking = smoking
        health_profile.Headaches = headaches
        health_profile.Asthma = asthma
        health_profile.Heart_problems = heart_problems
        health_profile.Cancer = cancer
        health_profile.Stroke = stroke
        health_profile.Bone_joint = bone_joint
        health_profile.Kidney_problem = kidney_problem
        health_profile.Liver_problems = liver_problems
        health_profile.Depression = depression
        health_profile.Allergies = allergies
        health_profile.Arthritis = arthritis
        health_profile.Pregnancy = pregnancy
        health_profile.Bmi = bmi
        health_profile.Bmi_category = bmi_category
        health_profile.save()

        return JsonResponse({'status': 'ok'})

    except KeyError:
        return JsonResponse({'error': 'Missing required fields or incorrect field names'})
    except (ValueError, TypeError):
        return JsonResponse({'error': 'Invalid data format'})
    except Exception as e:
        return JsonResponse({'error': str(e)})


def MySendComplaintPage(request):
    lid=request.POST['lid']
    com=request.POST['com']
    obj=Complaint()
    from datetime import datetime
    date=datetime.now().date().today()
    obj.Date=date
    obj.reply='pending'
    obj.complaint=com
    obj.USER=User.objects.get(LOGIN_id=lid)
    obj.save()
    return JsonResponse({'status': 'ok'})



def MySendfeedbacktPage(request):
    lid=request.POST['lid']
    feed=request.POST['com']
    obj=Feedback()
    from datetime import datetime
    date=datetime.now().date().today()
    obj.Date=date
    obj.Feedback=feed
    obj.USER=User.objects.get(LOGIN_id=lid)
    obj.save()
    return JsonResponse({'status': 'ok'})




def User_Viewreply(request):
    lid=request.POST['lid']
    s=Complaint.objects.filter(USER__LOGIN_id=lid)
    c=[]
    for i in s:
        c.append({'id':i.id, 'complaint':i.complaint, 'date':i.Date, 'reply':i.reply,'status':i.Status})

    return JsonResponse({'status': 'ok','data':c})





def User_Viewtips(request):
    s=Tips.objects.all().order_by('-id')

    c=[]
    for i in s:
        c.append({'id':i.id, 'date':i.Date,'title':i.Title, 'description':i.Description,"tname":i.TRAINER.Name})
    print(c)
    return JsonResponse({'status': 'ok','data':c})



def User_Viewtrainertips(request):
    tid=request.POST['trid']

    s=Tips.objects.filter(TRAINER__id=tid).order_by('-id')

    c=[]
    for i in s:
        c.append({'id':i.id, 'date':i.Date,'title':i.Title, 'description':i.Description})
    print(c)
    return JsonResponse({'status': 'ok','data':c})



def user_add_diet_profile(request):
    lid=request.POST['lid']
    weight=request.POST['weight']
    Height=request.POST['Height']
    Age=request.POST['age']
    Gender=request.POST['Gender']
    Obesity=request.POST['Obesity']
    Blood_pressure=request.POST['Blood_pressure']
    Diabetes=request.POST['Diabetes']
    Cholesterol=request.POST['Cholesterol']
    Alcohol_use=request.POST['Alcohol_use']
    Drug_use=request.POST['Drug_use']
    Smoking=request.POST['Smoking']
    Headaches=request.POST['Headaches']
    Asthma=request.POST['Asthma']
    Heart_problems=request.POST['Heart_problems']
    Cancer=request.POST['Cancer']
    Stroke=request.POST['Stroke']
    Bone_joint=request.POST['Bone_joint']
    Kidney_problem=request.POST['Kidney_problem']
    Liver_problems=request.POST['Liver_problems']
    Depression=request.POST['Depression']
    Allergies=request.POST['Allergies']
    Arthritis=request.POST['Arthritis']
    Pregnancy=request.POST['Pregnancy']

    the_height = float(Height)
    the_weight = float(weight)

    the_BMI = the_weight / (the_height / 100) ** 2

    print("Your Body Mass Index is",str(the_BMI)[:5])

    # if the_BMI <= 18.5:
    #     bmi=the_BMI[:5]
    # elif the_BMI <= 24.9:
    #     bmi=the_BMI[:5]
    # elif the_BMI <= 29.9:
    #     bmi=the_BMI[:5]
    # else:
    #     bmi=the_BMI[:5]

    if Health_profile.objects.filter(USER__LOGIN_id=lid).exists():
        return JsonResponse({'status': 'no'})

        # u = Health_profile.objects.get(USER__LOGIN_id =lid)
        # u.Height = Height
        # u.Weight = weight
        # u.Age = Age
        # u.Gender = Gender
        # u.Obesity = Obesity
        # u.Blood_pressure = Blood_pressure
        # u.Diabetes = Diabetes
        # u.Cholesterol = Cholesterol
        # u.Alcohol_use = Alcohol_use
        # u.Drug_use = Drug_use
        # u.Smoking = Smoking
        # u.Headaches = Headaches
        # u.Asthma = Asthma
        # u.Heart_problems = Heart_problems
        # u.Cancer = Cancer
        # u.Stroke = Stroke
        # u.Bone_joint = Bone_joint
        # u.Kidney_problem = Kidney_problem
        # u.Liver_problems = Liver_problems
        # u.Depression = Depression
        # u.Allergies = Allergies
        # u.Arthritis = Arthritis
        # u.Pregnancy=Pregnancy
        # u.Bmi=bmi
        # # u.USER = User.objects.get(LOGIN_id=lid)
        # u.save()
        # return JsonResponse({'status': 'ok'})

    u=Health_profile()
    u.Height=Height
    u.Weight=weight
    u.Age=Age
    u.Gender=Gender
    u.Obesity=Obesity
    u.Blood_pressure=Blood_pressure
    u.Diabetes=Diabetes
    u.Cholesterol=Cholesterol
    u.Alcohol_use=Alcohol_use
    u.Drug_use=Drug_use
    u.Smoking=Smoking
    u.Headaches=Headaches
    u.Asthma=Asthma
    u.Heart_problems=Heart_problems
    u.Cancer=Cancer
    u.Stroke=Stroke
    u.Bone_joint=Bone_joint
    u.Kidney_problem=Kidney_problem
    u.Liver_problems=Liver_problems
    u.Depression=Depression
    u.Allergies=Allergies
    u.Arthritis=Arthritis
    u.Pregnancy=Pregnancy
    u.Bmi=the_BMI
    u.USER=User.objects.get(LOGIN_id=lid)
    u.save()


    return JsonResponse({'status': 'ok'})



def user_removetrainer(request):
    Tid=request.POST['Tid']
    print(Tid,"ghhhhhhhhhhhhhh")
    res=Request.objects.filter(TRAINER__id=Tid).delete()
    # res=Tips.objects.filter(TRAINER__id=Tid).delete()
    # res=Diet_plan.objects.filter(TRAINER__id=Tid).delete()
    return JsonResponse({'status': 'ok'})



def user_viewhealthprofile(request):
    lid=request.POST['lid']
    res=Health_profile.objects.get(USER__LOGIN_id=lid)
    # print(res.Photo)
    return JsonResponse({"status":"ok",
                         "Height":res.Height,
                         "Weight":res.Weight,"Age":res.Age,
                         "Gender":res.Gender,"Obesity":res.Obesity,
                         "Blood_pressure":res.Blood_pressure,
                         "Diabetes":res.Diabetes,"Cholestrol":res.Cholesterol,
                         "Alcohol_use":res.Alcohol_use,"Drug_use":res.Drug_use,
                         "Smoking":res.Smoking,"Headaches":res.Headaches,
                         "Asthma":res.Asthma,"Heart_problem":res.Heart_problems,
                         "Cancer":res.Cancer,"Stroke":res.Stroke,
                         "Bone_joint":res.Bone_joint,"Kidney_problem":res.Kidney_problem,
                         "Liver_problem":res.Liver_problems,"Depression":res.Depression,
                         "Allergies":res.Allergies,"Arthritis":res.Arthritis,
                         "Pregnancy":res.Pregnancy,"Bmi":res.Bmi})



def user_edithealthprofile(request):
    lid=request.POST['lid']
    res=Health_profile.objects.get(USER__LOGIN_id=lid)
    # print(res.Photo)
    return JsonResponse({"status":"ok",
                         "Height":res.Height,
                         "Weight":res.Weight,"Age":res.Age,
                         "Gender":res.Gender,"Obesity":res.Obesity,
                         "Blood_pressure":res.Blood_pressure,
                         "Diabetes":res.Diabetes,"Cholestrol":res.Cholesterol,
                         "Alcohol_use":res.Alcohol_use,"Drug_use":res.Drug_use,
                         "Smoking":res.Smoking,"Headaches":res.Headaches,
                         "Asthma":res.Asthma,"Heart_problem":res.Heart_problems,
                         "Cancer":res.Cancer,"Stroke":res.Stroke,
                         "Bone_joint":res.Bone_joint,"Kidney_problem":res.Kidney_problem,
                         "Liver_problem":res.Liver_problems,"Depression":res.Depression,
                         "Allergies":res.Allergies,"Arthritis":res.Arthritis,
                         "Pregnancy":res.Pregnancy})

def Get_health_pr(request):
    lid = request.POST['lid']
    # lid = "19"

    d=Diet_chart.objects.all()

    if not Health_profile.objects.filter(USER__LOGIN_id=lid).exists():

        return JsonResponse({'status': 'no'})
    else:



        h=Health_profile.objects.get(USER__LOGIN_id=lid)

        features=[]
        label=[]




        test=[]


        obicity=0
        gender=0
        boodpressuree=0
        diabetes=0
        cholestrol=0
        alcoholabuse=0
        druguse=0
        smoking=0
        headaches=0
        asthma=0
        heartproblem=0
        cancer=0
        stroke=0
        kidney=0
        liver=0
        depression=0
        allergies=0
        arthritis=0
        pregnancy=0









        if  h.Obesity== "Normal":
            obicity=0
        elif h.Obesity=="OverWeight":
            obicity=1
        elif  h.Obesity=="Obesity":
            obicity=2




        if h.USER.Gender=="Male":
            gender=0
        elif h.USER.Gender=="Female":
            gender=1
        elif h.USER.Gender=="Others":
            gender=2




        if h.Blood_pressure=="Low":
            boodpressuree=0
        elif h.Blood_pressure=="Normal":
            boodpressuree=1
        elif h.Blood_pressure=="High":
            boodpressuree=2




        if h.Diabetes=="Low":
            diabetes=0
        elif h.Diabetes=="Normal":
            diabetes=1
        elif h.Diabetes=="High":
            diabetes=2




        if h.Cholesterol=="low-density lipoprotein":
            cholestrol=0
        elif h.Cholesterol=="high-density lipoprotein":
            cholestrol=1
        elif h.Cholesterol=="Lipoprotein Cholesterol":
            cholestrol=2




        if h.Alcohol_use=="Light or social drinkers":
            alcoholabuse=0
        elif h.Alcohol_use=="Moderate drinker":
            alcoholabuse=1
        elif h.Alcohol_use=="Heavy drinkers":
            alcoholabuse=2
        elif h.Alcohol_use=="No Use":
            alcoholabuse=3




        if h.Drug_use=="stimulants":
            druguse=0
        elif h.Drug_use=="narcotics":
            druguse=1
        elif h.Drug_use=="sedatives":
            druguse=2
        elif h.Drug_use=="No":
            druguse=3


        if h.Smoking=="No":
            smoking=0
        elif h.Smoking=="Yes":
            smoking=1




        if h.Headaches=="No":
            headaches=0
        elif h.Headaches=="Yes":
            headaches=1



        if h.Asthma=="No":
            asthma=0
        elif h.Asthma=="Yes":
            asthma=1



        if h.Heart_problems=="No":
            heartproblem=0
        elif h.Heart_problems=="Yes":
            heartproblem=1




        if h.Cancer=="No":
            cancer=0
        elif h.Cancer=="Yes":
            cancer=1



        if h.Stroke=="No":
            stroke=0
        elif h.Stroke=="Yes":
            stroke=1


        if h.Kidney_problem=="No":
            kidney=0
        elif h.Kidney_problem=="Yes":
            kidney=1


        if h.Liver_problems=="No":
            liver=0
        elif h.Liver_problems=="Yes":
            liver=1


        if h.Depression=="No":
            depression=0
        elif h.Depression=="Yes":
            depression=1


        if h.Allergies=="No":
            allergies=0
        elif h.Allergies=="Yes":
            allergies=1


        if h.Arthritis=="No":
            arthritis=0
        elif h.Arthritis=="Yes":
            arthritis=1


        if h.Pregnancy=="No":
            pregnancy=0
        elif h.Pregnancy=="Yes":
            pregnancy=1








        test=[
            gender,
            obicity,
            boodpressuree,
            diabetes,
            cholestrol,
            alcoholabuse,
            druguse,
            smoking,
            headaches,
            asthma,
            heartproblem,
            cancer,
            stroke,
            kidney,
            liver,
            depression,
            allergies,
            arthritis,
            pregnancy,
            h.Bmi,

        ]





        for i in d:

            label.append(i.id)


            if i.Gender=="Male":
                gender=0
            elif i.Gender=="Female":
                gender = 1


            if i.Obesity=="Normal":
                obicity=0
            elif i.Obesity=="OverWeight":
                obicity = 1
            elif i.Obesity=="Obesity":
                obicity = 2


            if i.Blood_pressure=="Low":
                boodpressuree=0
            elif i.Blood_pressure=="Normal":
                boodpressuree = 1
            elif i.Blood_pressure=="High":
                boodpressuree = 2


            if i.Diabetes=="Low":
                diabetes=0
            elif i.Diabetes=="Normal":
                diabetes = 1
            elif i.Diabetes=="High":
                diabetes = 2


            if i.Cholesterol=="low-density lipoprotein(LDL)":
                cholestrol=0
            elif i.Cholesterol=="high-density lipoprotein (HDL)":
                cholestrol = 1
            elif i.Cholesterol=="Lipoprotein(a) Cholesterol":
                cholestrol = 2



            if i.Alcohol_use=="Light or social drinkers":
                alcoholabuse=0
            elif i.Alcohol_use=="Moderate drinker":
                alcoholabuse = 1
            elif i.Alcohol_use=="Heavy drinkers":
                alcoholabuse = 2
            elif i.Alcohol_use == "No Use":
                alcoholabuse = 3


            if i.Drug_use=="stimulants":
                druguse=0
            elif i.Drug_use=="narcotics":
                druguse = 1
            elif i.Drug_use=="Heavy drinkers":
                druguse = 2
            elif i.Drug_use == "No Use":
                druguse = 3


            if i.Smoking=="No":
                smoking=0
            elif i.Smoking=="Yes":
                smoking = 1


            if i.Headaches=="No":
                headaches=0
            elif i.Headaches=="Yes":
                headaches = 1



            if i.Asthma=="No":
                asthma=0
            elif i.Asthma=="Yes":
                asthma = 1


            if i.Heart_problems=="No":
                heartproblem=0
            elif i.Heart_problems=="Yes":
                heartproblem = 1


            if i.Cancer=="No":
                cancer=0
            elif i.Cancer=="Yes":
                cancer = 1


            if i.Stroke=="No":
                stroke=0
            elif i.Stroke=="Yes":
                stroke = 1


            if i.Kidney_problem=="No":
                kidney=0
            elif i.Kidney_problem=="Yes":
                kidney = 1


            if i.Liver_problems=="No":
                liver=0
            elif i.Liver_problems=="Yes":
                liver = 1


            if i.Depression=="No":
                depression=0
            elif i.Depression=="Yes":
                depression = 1


            if i.Allergies=="No":
                allergies=0
            elif i.Allergies=="Yes":
                allergies = 1


            if i.Arthritis=="No":
                arthritis=0
            elif i.Arthritis=="Yes":
                arthritis = 1



            if i.Pregnancy=="No":
                pregnancy=0
            elif i.Allergies=="Yes":
                pregnancy = 1





            # bmi not given!





            features.append(
                [
                    gender,
                    obicity,
                    boodpressuree,
                    diabetes,
                    cholestrol,
                    alcoholabuse,
                    druguse,
                    smoking,
                    headaches,
                    asthma,
                    heartproblem,
                    cancer,
                    stroke,
                    kidney,
                    liver,
                    depression,
                    allergies,
                    arthritis,
                    pregnancy,
                    i.Bmi,

                ]
            )



        from sklearn.ensemble import  RandomForestClassifier

        r=RandomForestClassifier()

        r.fit(features,label)

        s=r.predict_proba([test])

        print(s)

        s=s[0]

        ls=[]

        for i in range(0,len(s)):

            dietid=label[i]



            if s[i]>.2:    #change according to the BMI value to get tha diet chart to user

                ss=Diet_chart.objects.get(id=dietid)

                ls.append(
                    {
                        'id':ss.id,
                        # 'name':ss.Name,
                        'date':ss.Date,
                        'time':ss.Time,
                        'dietplan':ss.menu,
                        'quantity':ss.quantity

                    }
                )


        return JsonResponse({'status': 'ok','data':ls})


def Get_trainerhealth_pr(request):
    lid = request.POST['lid']
    tid = request.POST['trid']
    # lid = "19"

    d=Diet_chart.objects.filter(TRAINER__id=tid)

    if not Health_profile.objects.filter(USER__LOGIN_id=lid).exists():

        return JsonResponse({'status': 'no'})
    else:



        h=Health_profile.objects.get(USER__LOGIN_id=lid)

        features=[]
        label=[]




        test=[]


        obicity=0
        gender=0
        boodpressuree=0
        diabetes=0
        cholestrol=0
        alcoholabuse=0
        druguse=0
        smoking=0
        headaches=0
        asthma=0
        heartproblem=0
        cancer=0
        stroke=0
        kidney=0
        liver=0
        depression=0
        allergies=0
        arthritis=0
        pregnancy=0









        if  h.Obesity== "Normal":
            obicity=0
        elif h.Obesity=="OverWeight":
            obicity=1
        elif  h.Obesity=="Obesity":
            obicity=2




        if h.USER.Gender=="Male":
            gender=0
        elif h.USER.Gender=="Female":
            gender=1
        elif h.USER.Gender=="Others":
            gender=2




        if h.Blood_pressure=="Low":
            boodpressuree=0
        elif h.Blood_pressure=="Normal":
            boodpressuree=1
        elif h.Blood_pressure=="High":
            boodpressuree=2




        if h.Diabetes=="Low":
            diabetes=0
        elif h.Diabetes=="Normal":
            diabetes=1
        elif h.Diabetes=="High":
            diabetes=2




        if h.Cholesterol=="low-density lipoprotein":
            cholestrol=0
        elif h.Cholesterol=="high-density lipoprotein":
            cholestrol=1
        elif h.Cholesterol=="Lipoprotein Cholesterol":
            cholestrol=2




        if h.Alcohol_use=="Light or social drinkers":
            alcoholabuse=0
        elif h.Alcohol_use=="Moderate drinker":
            alcoholabuse=1
        elif h.Alcohol_use=="Heavy drinkers":
            alcoholabuse=2
        elif h.Alcohol_use=="No Use":
            alcoholabuse=3




        if h.Drug_use=="stimulants":
            druguse=0
        elif h.Drug_use=="narcotics":
            druguse=1
        elif h.Drug_use=="sedatives":
            druguse=2
        elif h.Drug_use=="No":
            druguse=3


        if h.Smoking=="No":
            smoking=0
        elif h.Smoking=="Yes":
            smoking=1




        if h.Headaches=="No":
            headaches=0
        elif h.Headaches=="Yes":
            headaches=1



        if h.Asthma=="No":
            asthma=0
        elif h.Asthma=="Yes":
            asthma=1



        if h.Heart_problems=="No":
            heartproblem=0
        elif h.Heart_problems=="Yes":
            heartproblem=1




        if h.Cancer=="No":
            cancer=0
        elif h.Cancer=="Yes":
            cancer=1



        if h.Stroke=="No":
            stroke=0
        elif h.Stroke=="Yes":
            stroke=1


        if h.Kidney_problem=="No":
            kidney=0
        elif h.Kidney_problem=="Yes":
            kidney=1


        if h.Liver_problems=="No":
            liver=0
        elif h.Liver_problems=="Yes":
            liver=1


        if h.Depression=="No":
            depression=0
        elif h.Depression=="Yes":
            depression=1


        if h.Allergies=="No":
            allergies=0
        elif h.Allergies=="Yes":
            allergies=1


        if h.Arthritis=="No":
            arthritis=0
        elif h.Arthritis=="Yes":
            arthritis=1


        if h.Pregnancy=="No":
            pregnancy=0
        elif h.Pregnancy=="Yes":
            pregnancy=1








        test=[
            gender,
            obicity,
            boodpressuree,
            diabetes,
            cholestrol,
            alcoholabuse,
            druguse,
            smoking,
            headaches,
            asthma,
            heartproblem,
            cancer,
            stroke,
            kidney,
            liver,
            depression,
            allergies,
            arthritis,
            pregnancy,
            h.Bmi,

        ]





        for i in d:

            label.append(i.id)


            if i.Gender=="Male":
                gender=0
            elif i.Gender=="Female":
                gender = 1


            if i.Obesity=="Normal":
                obicity=0
            elif i.Obesity=="OverWeight":
                obicity = 1
            elif i.Obesity=="Obesity":
                obicity = 2


            if i.Blood_pressure=="Low":
                boodpressuree=0
            elif i.Blood_pressure=="Normal":
                boodpressuree = 1
            elif i.Blood_pressure=="High":
                boodpressuree = 2


            if i.Diabetes=="Low":
                diabetes=0
            elif i.Diabetes=="Normal":
                diabetes = 1
            elif i.Diabetes=="High":
                diabetes = 2


            if i.Cholesterol=="low-density lipoprotein(LDL)":
                cholestrol=0
            elif i.Cholesterol=="high-density lipoprotein (HDL)":
                cholestrol = 1
            elif i.Cholesterol=="Lipoprotein(a) Cholesterol":
                cholestrol = 2



            if i.Alcohol_use=="Light or social drinkers":
                alcoholabuse=0
            elif i.Alcohol_use=="Moderate drinker":
                alcoholabuse = 1
            elif i.Alcohol_use=="Heavy drinkers":
                alcoholabuse = 2
            elif i.Alcohol_use == "No Use":
                alcoholabuse = 3


            if i.Drug_use=="stimulants":
                druguse=0
            elif i.Drug_use=="narcotics":
                druguse = 1
            elif i.Drug_use=="Heavy drinkers":
                druguse = 2
            elif i.Drug_use == "No Use":
                druguse = 3


            if i.Smoking=="No":
                smoking=0
            elif i.Smoking=="Yes":
                smoking = 1


            if i.Headaches=="No":
                headaches=0
            elif i.Headaches=="Yes":
                headaches = 1



            if i.Asthma=="No":
                asthma=0
            elif i.Asthma=="Yes":
                asthma = 1


            if i.Heart_problems=="No":
                heartproblem=0
            elif i.Heart_problems=="Yes":
                heartproblem = 1


            if i.Cancer=="No":
                cancer=0
            elif i.Cancer=="Yes":
                cancer = 1


            if i.Stroke=="No":
                stroke=0
            elif i.Stroke=="Yes":
                stroke = 1


            if i.Kidney_problem=="No":
                kidney=0
            elif i.Kidney_problem=="Yes":
                kidney = 1


            if i.Liver_problems=="No":
                liver=0
            elif i.Liver_problems=="Yes":
                liver = 1


            if i.Depression=="No":
                depression=0
            elif i.Depression=="Yes":
                depression = 1


            if i.Allergies=="No":
                allergies=0
            elif i.Allergies=="Yes":
                allergies = 1


            if i.Arthritis=="No":
                arthritis=0
            elif i.Arthritis=="Yes":
                arthritis = 1



            if i.Pregnancy=="No":
                pregnancy=0
            elif i.Allergies=="Yes":
                pregnancy = 1





            # bmi not given!





            features.append(
                [
                    gender,
                    obicity,
                    boodpressuree,
                    diabetes,
                    cholestrol,
                    alcoholabuse,
                    druguse,
                    smoking,
                    headaches,
                    asthma,
                    heartproblem,
                    cancer,
                    stroke,
                    kidney,
                    liver,
                    depression,
                    allergies,
                    arthritis,
                    pregnancy,
                    i.Bmi,

                ]
            )



        from sklearn.ensemble import  RandomForestClassifier

        r=RandomForestClassifier()

        r.fit(features,label)

        s=r.predict_proba([test])

        print(s)

        s=s[0]

        ls=[]

        for i in range(0,len(s)):

            dietid=label[i]



            if s[i]>.2:    #change according to the BMI value to get tha diet chart to user

                ss=Diet_chart.objects.get(id=dietid)

                import datetime
                parsed_time = datetime.datetime.strptime(ss.Time, '%H:%M')
                formatted_time = parsed_time.strftime('%I:%M %p')
                ls.append(
                    {
                        'id':ss.id,
                        # 'name':ss.Name,
                        'date':ss.Date,
                        'time':formatted_time,
                        'dietplan':ss.menu,
                        'quantity':ss.quantity

                    }
                )


        return JsonResponse({'status': 'ok','data':ls})
