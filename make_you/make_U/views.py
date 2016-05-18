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


            return redirect(result_join )




    return render(request,'join_form.html')

def check_overlap(request,checking_id):
    checked = 0
    if request.method =='POST':
        try:
            checked_id = request.POST.get('re_check_id')
            User.objects.get(username = checked_id)
            checked = 0
        except  ObjectDoesNotExist:
            checked = 1
        ctx={
            'checked' : checked,
            'checked_id' : checked_id,
        }

        return render(request,'check_overlap.html',ctx)


    try:
        User.objects.get(username = checking_id)
        checked = 0
    except  ObjectDoesNotExist:
        checked = 1
    ctx={
        'checked' : checked,
        'checked_id' : checking_id,
    }

    return render(request,'check_overlap.html',ctx)

def result_join(request):
    if request.method == 'POST':


        return redirect(edit)
    username = request.user.username
    ctx={
            'username' : username
        }
    return render(request,'result_join.html',ctx)

@login_required
def edit(request):
    if request.method == 'POST':
        try:
            origin_contents = Contents.objects.get(user = request.user)
            origin_contents.summary = request.POST.get('summary')
            origin_contents.work_exp = request.POST.get('work_exp')

            origin_contents.save()
            return redirect(select_temp)

        except  ObjectDoesNotExist:
            new_contents = Contents(
            summary = request.POST.get('summary'),
            work_exp = request.POST.get('work_exp'),
            )
            new_contents.user = request.user
            new_contents.save()

            return redirect(select_temp)

    try:
        origin_content = Contents.objects.get(user = request.user)
        username = request.user.username
        ctx={
            'content' : origin_content,
            'username' : username,
        }
        return render(request,'edit.html',ctx)
    except  ObjectDoesNotExist:
        username = request.user.username
        ctx={
            'username' : username
        }
        return render(request,'edit.html',ctx)

@login_required
def select_temp(request):
    if request.method == 'POST':
        template_num = request.POST.get('template_num')
        origin_contents = Contents.objects.get(user = request.user)
        origin_contents.template_id = template_num
        origin_contents.save()

        return redirect(pre_view)


    templates = Templates.objects.all()


    username = request.user.username
    ctx={
        'username' : username,
        'templates' : templates,

    }
    return render(request,'select_temp.html',ctx)

@login_required
def pre_view(request):

    try:
        user_contents = Contents.objects.get(user = request.user)
    except  ObjectDoesNotExist:


        return redirect(edit)

    template_html ='template_{t_id}.html'.format(
        t_id = user_contents.template_id
        )
    user_full_name = request.user.get_full_name()

    ctx = {
        'content' : user_contents,
        'user_full_name' : user_full_name,
    }
    return render(request,template_html,ctx)
