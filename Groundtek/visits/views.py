from visits.forms import OrderService, OrderForm, OrderCall, LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm
from visits.visits import Visits
from visits.models import Visitors,Profile
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, UserRegistrationForm
from standart.models import Navconstruct

@login_required
def dashboard(request):
    return render(request, 'standart/user/dashboard.html', {})



def check(request):
    t=Visits(request).see()
    Visitors.objects.update(lastupdate=t['LastIP'])
    return HttpResponse(status=200)


def user_login(request):
    nid = Navconstruct.objects.first()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'standart/user/login.html', {'form': form,'nid':nid})


def register(request):
    nid = Navconstruct.objects.first()
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            profile = Profile.objects.create(user=new_user)
            return render(request, 'standart/user/register_done.html', {'new_user': new_user,'nid':nid})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'standart/user/register.html', {'user_form': user_form,'nid':nid})


@login_required
def edit(request):
    nid = Navconstruct.objects.first()
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return render(request, 'standart/user/dashboard.html', {'nid':nid})

    else:
        user_form = UserEditForm(instance=request.user)
        try:
            profile_form = ProfileEditForm(instance=request.user.profile)
        except:
            return render(request, 'standart/user/dashboard.html', {'nid':nid})
        return render(request,
                      'standart/user/edit.html',
                      {'user_form': user_form,
                       'profile_form': profile_form,'nid':nid})