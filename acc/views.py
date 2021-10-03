from django.shortcuts import redirect, render
from .models import User
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as login_process

# Create your views here.
def index(request):
    return render(request, "index.html")

def login(request):
    if request.user.username:
        return redirect('acc:index')
    if request.method == "POST":
        u = request.POST.get("username")
        p = request.POST.get("password")
        user = authenticate(username=u, password=p)
        if user:
            login_process(request, user)
            return redirect("acc:index")
    return render(request, "acc/login.html")

def signup(request):
    if request.user.username:
        return redirect('acc:index')
    if request.method == "POST":
        u = request.POST.get("username")
        p = request.POST.get("password")
        n = request.POST.get("nickname")
        a = request.POST.get("age")
        c = request.POST.get("comment")
        i = request.FILES.get("image")
        if not i:
            i = 'none.png'
        User.objects.create_user(username=u, password=p, nickname=n, age=a, comment=c, pic=i).save()
        return redirect("acc:login")
    return render(request, "acc/signup.html")

def logout_user(request):
    logout(request)
    return redirect('acc:index')

def profile(request):
    if not(request.user.username):
        return redirect('acc:login')
    return render(request, 'acc/profile.html')

def update(request):
    if not(request.user.username):
        return redirect('acc:login')
    if request.method == "POST":
        u = request.user.username
        user = User.objects.get(username=u)
        p = request.POST.get("password")
        if p:
            user.set_password(p)
        user.nickname = request.POST.get("nickname")
        user.age = request.POST.get("age")
        user.comment = request.POST.get("comment")
        i = request.FILES.get("image")
        if i:
            user.pic = i
        user.save()
        user = authenticate(username=u, password=p)
        login_process(request, user)
        return redirect('acc:profile')

    return render(request, 'acc/update.html')

def delete(request):
    if not(request.user.username):
        return redirect('acc:index')
    u = request.user.username
    user = User.objects.get(username=u)
    user.delete()
    return redirect('acc:index')