from django.shortcuts import render
from django.shortcuts import redirect
from .models import Contents
from .models import Templates
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

@login_required
def main(request):
    '''if request.method == "POST":
        login_username = request.POST.get('id')
        login_password = request.POST.get('password')
        user = authenticate(username=login_username,password=login_password)
        if user is not None:
            login(request, user)
            return render(request,'main.html',ctx)

        else:
            return redirect('login')'''

    username = request.user.username
    ctx={

        'username' : username,
    }
    return render(request,'main.html',ctx)

def join(request):
    if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            new_user = User.objects.create_user(
                username = username,
                password = password,
                is_superuser = False,
                first_name =  request.POST.get('first_name'),
                last_name =  request.POST.get('last_name'),
                email = 'null',
                is_staff = False,
                is_active = True,
            )
            new_user.save()
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)

            username = username
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

@login_required
def edit(request, username):
    if request.method == 'POST':
        try:
            User.objects.get(pk = request.user.pk)

            origin_contents = Contents.objects.get(user = request.user)
            origin_contents.summary = request.POST.get('summary')
            origin_contents.work_exp = request.POST.get('work_exp')

            origin_contents.save()
            return redirect(select_temp,username)

        except  ObjectDoesNotExist:
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

@login_required
def select_temp(request, username):
    if request.method == 'POST':
        template_num = request.POST.get('template_num')
        origin_contents = Contents.objects.get(user = request.user)
        origin_contents.template_id = template_num
        origin_contents.save()

        return redirect(pre_view, template_num)


    templates = Templates.objects.all()



    ctx={
        'username' : username,
        'templates' : templates,

    }
    return render(request,'select_temp.html',ctx)

@login_required
def pre_view(request):
    origin_contents = Contents.objects.get(user = request.user)

    ctx = {
        'content' : origin_contents
    }
    return render(request,'result_pre_view.html',ctx)
