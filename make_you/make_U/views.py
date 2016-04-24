from django.shortcuts import render
from django.shortcuts import redirect
from .models import Contents
from .models import Templates
from django.conf import settings
from django.shortcuts import get_object_or_404


def main(request):
    ctx={}
    return render(request,'main.html',ctx)

def join(request):
    if request.method == "POST":

            '''new_user = settings.AUTH_USER_MODEL(
                username = request.POST.get('username'),
                password = request.POST.get('password'),
                is_superuser = False,
                first_name =  request.POST.get('first_name'),
                last_name =  request.POST.get('last_name'),
                email = 'null',
                is_staff = False,
                is_active = 1,
            )
            new_user.save()'''
            username = request.POST.get('username')
            return redirect(result_join, username )




    return render(request,'join_form.html')

def result_join(request, username):
    if request.method == 'POST':
        username = username

        return redirect(edit, username)
    ctx={
        'username' : username,
        }
    return render(request,'result_join.html',ctx)

def edit(request, username):
    if request.method == 'POST':
        new_contents = Contents(
            summary = request.POST.get('summary'),
            work_exp = request.POST.get('work_exp'),
        )
        new_contents.user = request.user
        new_contents.save()

        return redirect(select_temp,username)

    ctx={
        'username' :username,
    }
    return render(request,'edit.html',ctx)

def select_temp(request, username):
    if request.method == 'POST':
        template_num = request.POST.get('template_num')
        return redirect(pre_view, template_num)


    templates = Templates.objects.all()
    ctx={
        'username' : username,
        'templates' : templates
    }
    return render(request,'select_temp.html',ctx)

def pre_view(request, template_num):
    ctx = {

    }
    return render(request,'result_pre_view.html',ctx)
