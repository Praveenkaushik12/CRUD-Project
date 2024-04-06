from django.shortcuts import render,HttpResponseRedirect
from .forms import StudentRegistration
from .models import User

# Create your views here.
def add_show(request):
    if request.method=='POST':
        fm=StudentRegistration(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            pwd=fm.cleaned_data['password']
            reg=User(name=nm,email=em,password=pwd)
            reg.save()
        fm=StudentRegistration()
    else:
        fm=StudentRegistration()
    students=User.objects.all()
    return render(request,'enroll/addandshow.html',{'form':fm,'stu':students})

def delete_data(request,id):
    if request.method=='POST':
        stud=User.objects.get(pk=id)
        stud.delete()
    return HttpResponseRedirect('/')

def update_data(request,id):
    if request.method=='POST':
        stud=User.objects.get(pk=id)
        fm=StudentRegistration(request.POST,instance=stud)
        if fm.is_valid():
            fm.save()
        return HttpResponseRedirect('/')
    else:
        stud=User.objects.get(pk=id)
        fm=StudentRegistration(instance=stud)       
    return render(request,'enroll/updatestudent.html',{'form':fm})