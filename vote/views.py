from django.http import request
from django.shortcuts import redirect, render
from .models import *

# Create your views here.
def index(request):
    t = Topic.objects.all()
    context = {
        'con' : t
    }
    return render(request, 'vote/index.html', context)

def create(request):
    if request.method == "POST":
        title = request.POST.get("title")
        writer = request.user.username
        writer_pic = request.user.pic
        comment = request.POST.get("comment")
        names = request.POST.getlist("name")
        pics = request.FILES.getlist("pic")
        if title and names and pics:
            t = Topic(title=title, writer=writer, writer_pic=writer_pic, comment=comment)
            t.save()
            for i, j in zip(names, pics):
                Choice(title=t, name=i, pic=j).save()
        return redirect("vote:index")
    return render(request, "vote/create.html")

def detail(request, num):
    t = Topic.objects.get(id=num)
    c= t.choice_set.all()
    context = {
        'con' : t,
        'cho' : c
    }
    return render(request, "vote/detail.html", context)

def vote(request, conid):
    t = Topic.objects.get(id=conid)
    vc = request.POST.get('vote_cancel')
    if vc == "vote":
        if not request.user in t.voter.all():
            t.voter.add(request.user)
            n = request.POST.get("name")
            c = Choice.objects.get(id=n)
            c.choicer.add(request.user)
    elif vc == "cancel":
        if request.user in t.voter.all():
            t.voter.remove(request.user)
            choices = t.choice_set.all()
            for i in choices:
                if request.user in i.choicer.all():
                    i.choicer.remove(request.user)
    return redirect('vote:detail', num=conid)