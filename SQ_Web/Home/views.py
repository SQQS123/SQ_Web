from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from .forms import UserRegisterForm, UserLoginForm
from .models import Users


# Registered users can do more
def register(request):
    context = dict()
    form = UserRegisterForm()
    if request.method == "POST":
        url_name = 'register_fail'
        form = UserRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            result = form.save()
            if result:
                url_name = 'register_success'
        else:
            context['form'] = form
            return render(request, "Home/register_fail.html", context)
        return HttpResponseRedirect(reverse("Home:" + url_name))
    context['form'] = form
    return render(request, "Home/register.html", context)


# Register successfully
def user_register_success(request):
    context = dict()
    return render(request, "Home/register_success.html", context)


def user_register_fail(request):
    context = dict()
    return render(request, "Home/register_fail.html", context)


# But you have to login at first
def login(request):
    context = dict()
    request.session['IS_LOGIN'] = False
    form = UserLoginForm()
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = Users.objects.filter(username=username, password=password)
            if user:
                user = user[0]
                login_user = dict(username=user.username,
                                  portrait=str(user.portrait),
                                  nickname=user.nickname)
                request.session['login_user'] = login_user
                request.session['IS_LOGIN'] = True
                context["user"] = user
                # go to personal homepage
                # return HttpResponseRedirect(reverse("Home:" + "home",request))
                print(request.session["IS_LOGIN"])
                return render(request, 'Home/Home.html', context)
            else:
                context['error_message'] = "账号或密码错误！"

    context['form'] = form
    return render(request, "Home/login.html", context)


# the decorator to chek login
def check_login(func):
    def wrapper(request, *args, **kwargs):
        is_login=request.session.get('IS_LOGIN', False)
        if is_login:
            return func(request, *args, **kwargs)
        else:
            return redirect('login/')
    return wrapper


# We'll see homepage first

def home(request):
    request.session["IS_LOGIN"] = False
    return render(request, 'Home/Home.html')