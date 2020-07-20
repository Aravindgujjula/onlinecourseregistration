from django.shortcuts import render,redirect
from django.contrib import messages
from django.views.generic import UpdateView
from django.core.paginator import Paginator

from appcourse.models import centermodel,studentregistration
from appcourse.forms import centerform,studentform
# Create your views here.


def admin_login(request):
    return render(request,"admin_login.html")


def admin_login_check(request):
    un = request.POST.get("t1")
    up = request.POST.get("t2")
    if un == "Aravind" and up == "Aravind":
        return render(request,"admin_welcome.html")
    else:
        messages.error(request,"Invalid User")
        return redirect('admin_login')


def schedule_class(request):
    cm = centerform
    return render(request,"schedule_class.html",{"form": cm})




def save_class(request):

    form=centerform

    if request.method=='POST':

        form=centerform(request.POST)

        if form.is_valid():

            form.save()

            return redirect('schedule_class')

    return render(request,'schedule_class.html',{'form':form})


def View_all(request):
    data = centermodel.objects.all()
    return render(request,"viewall_classes.html",{'form':data})



def update(request):
    no = request.GET.get("cid")
    res = centermodel.objects.get(no=no)
    return  render(request, 'update.html',{'data':res})




def update_course(request):
    no = request.POST.get("u1")
    na = request.POST.get("u2")
    fna = request.POST.get("u3")
    da = request.POST.get("u4")
    ti = request.POST.get("u5")
    fe = request.POST.get("u6")
    du = request.POST.get("u7")

    centermodel.objects.filter(no=no).update(course_name=na, faculty=fna, date=da, time=ti, fee=fe, duration=du)

    return redirect('View_all')

def delete(request):
    no = request.GET.get("cid")
    # Query to delete 1 record from DB
    centermodel.objects.filter(no=no).delete()
    return redirect('View_all')


def main(request):

    res = centermodel.objects.all()

    return render(request,"main.html",{"data":res})


def course(request):
    data = centermodel.objects.all()
    return render(request, "course.html", {'data': data})


def register(request):
    sm = studentform

    return render(request,"register.html",{"form":sm})


def save_reg(request):

    form = studentform

    if request.method == "POST":
        form = studentform(request.POST)
        if form.is_valid():
            form.save()
            return  redirect('register')
    return render(request,"register.html",{'form':form})


def login(request):
    return render(request, 'student_login.html')


def student_login_check(request):
    un = request.GET.get('t1')
    up = request.GET.get('t2')

    try:
        s = studentregistration.objects.get(Name=un,Password=up)
        if un == s.Name and up == s.Password:
            return render(request,"student_home.html")
    except studentregistration.DoesNotExist:
        messages.error(request, "Invalid User")
        return redirect('login')


def enroll(request):
    #
    data = centermodel.objects.all()
    return render(request,"enroll.html",{"form":data})

def viewenroll(request):
    cm = centermodel
    sm = studentregistration
    studentregistration.objects.get("Contactno")


    no = request.GET.get("cid")

    data = centermodel.objects.get(no=no)
    return render(request,"enroll.html",{"form":data})
