from django.db import models

# Create your models here.
class Login(models.Model):
    Username=models.CharField(max_length=100)
    Password=models.CharField(max_length=100)
    Type=models.CharField(max_length=100)


class Trainer(models.Model):
    Name=models.CharField(max_length=100)
    EmaiL=models.CharField(max_length=100)
    Phone=models.CharField(max_length=100)
    Post=models.CharField(max_length=100)
    Pin=models.CharField(max_length=20)
    Dob=models.DateField()
    Gender=models.CharField(max_length=100)
    Photo=models.CharField(max_length=500)
    PLACE=models.CharField(max_length=100)
    Experience=models.CharField(max_length=100,default="")
    Status=models.CharField(max_length=20, default='pending')
    LOGIN=models.ForeignKey(Login,on_delete=models.CASCADE)


class User(models.Model):
    Name=models.CharField(max_length=100)
    EmaiL = models.CharField(max_length=100)
    Phone = models.CharField(max_length=100)
    Post = models.CharField(max_length=100)
    Pin = models.CharField(max_length=20)
    Dob = models.DateField()
    Gender = models.CharField(max_length=100)
    Photo = models.CharField(max_length=500)
    PLACE = models.CharField(max_length=100)
    LOGIN = models.ForeignKey(Login, on_delete=models.CASCADE)


class Tips(models.Model):
    Date=models.DateField()
    Title=models.CharField(max_length=100)
    Description=models.CharField(max_length=10000)
    TRAINER=models.ForeignKey(Trainer,on_delete=models.CASCADE)

class Request(models.Model):
    Date=models.DateField()
    TRAINER=models.ForeignKey(Trainer,on_delete=models.CASCADE)
    USER=models.ForeignKey(User,on_delete=models.CASCADE)
    Status=models.CharField(max_length=100)


class Health_profile(models.Model):
    Height=models.CharField(max_length=100)
    Weight=models.CharField(max_length=100)
    Age = models.CharField(max_length=100,default="")
    Gender= models.CharField(max_length=100,default="")
    Obesity = models.CharField(max_length=100)
    Blood_pressure=  models.CharField(max_length=100)
    Diabetes=  models.CharField(max_length=100)
    Cholesterol=  models.CharField(max_length=100)
    Alcohol_use=  models.CharField(max_length=100)
    Drug_use=  models.CharField(max_length=100)
    Smoking=  models.CharField(max_length=100)
    Headaches=  models.CharField(max_length=100)
    Asthma=  models.CharField(max_length=100)
    Heart_problems=  models.CharField(max_length=100)
    Cancer=  models.CharField(max_length=100)
    Stroke=  models.CharField(max_length=100)
    Bone_joint=  models.CharField(max_length=100)
    Kidney_problem=  models.CharField(max_length=100)
    Liver_problems=  models.CharField(max_length=100)
    Depression=  models.CharField(max_length=100)
    Allergies=  models.CharField(max_length=100)
    Arthritis=  models.CharField(max_length=100)
    Pregnancy=  models.CharField(max_length=100)
    Bmi =  models.CharField(max_length=100)
    USER=models.ForeignKey(User,on_delete=models.CASCADE)

class Diet_plan(models.Model):
    Date= models.DateField()
    menu=models.CharField(max_length=100)
    quantity=models.CharField(max_length=100)
    TRAINER=models.ForeignKey(Trainer,on_delete=models.CASCADE)
    time=models.CharField(max_length=100)


class Diet_chart(models.Model):
    Height = models.CharField(max_length=100)
    Weight = models.CharField(max_length=100)
    Age = models.CharField(max_length=100, default="")
    Gender = models.CharField(max_length=100, default="")
    Obesity = models.CharField(max_length=100)
    Blood_pressure = models.CharField(max_length=100)
    Diabetes = models.CharField(max_length=100)
    Cholesterol = models.CharField(max_length=100)
    Alcohol_use = models.CharField(max_length=100)
    Drug_use = models.CharField(max_length=100)
    Smoking = models.CharField(max_length=100)
    Headaches = models.CharField(max_length=100)
    Asthma = models.CharField(max_length=100)
    Heart_problems = models.CharField(max_length=100)
    Cancer = models.CharField(max_length=100)
    Stroke = models.CharField(max_length=100)
    Bone_joint = models.CharField(max_length=100)
    Kidney_problem = models.CharField(max_length=100)
    Liver_problems = models.CharField(max_length=100)
    Depression = models.CharField(max_length=100)
    Allergies = models.CharField(max_length=100)
    Arthritis = models.CharField(max_length=100)
    Pregnancy = models.CharField(max_length=100)
    Bmi = models.CharField(max_length=100)
    Date = models.CharField(max_length=100,default='')
    menu = models.CharField(max_length=100,default='')
    quantity = models.CharField(max_length=100,default='')
    TRAINER=models.ForeignKey(Trainer,on_delete=models.CASCADE,default='')
    Time=models.CharField(max_length=100)



class Complaint(models.Model):
    complaint=models.CharField(max_length=100)
    Date= models.DateField()
    reply=models.CharField(max_length=800)
    Status = models.CharField(max_length=20, default='pending')
    USER = models.ForeignKey(User, on_delete=models.CASCADE)

class Feedback(models.Model):
    Feedback=models.CharField(max_length=100)
    Date=models.DateField()
    USER = models.ForeignKey(User, on_delete=models.CASCADE)


class Chat(models.Model):
    message=models.CharField(max_length=100)
    Date= models.DateField()
    Time= models.CharField(max_length=100)
    FROMID=models.ForeignKey(Login,on_delete=models.CASCADE,related_name='from_id')
    TOID=models.ForeignKey(Login,on_delete=models.CASCADE,related_name='to_id')


