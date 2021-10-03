from django.shortcuts import redirect, render
from .models import Board, Reply
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    kw = request.GET.get('kw','')
    cate = request.GET.get('cate','')
    page = request.GET.get('page', 1)

    if kw:
        if cate == 'subject':
            b = Board.objects.filter(subject__startswith=kw)
        elif cate == 'writer':
            b = Board.objects.filter(writer__startswith=kw)
        else:
            b = Board.objects.filter(content__contains=kw)
    else:
        b = Board.objects.all()

    pag = Paginator(b, 10)
    obj = pag.get_page(page)
    context={
        'con' : obj,
        'cate' : cate,
        'kw' : kw,
    }
    return render(request, "bd/index.html", context)

def create(request):
    if not(request.user.username):
        return redirect('acc:index')
    if request.method == "POST":
        print("a")
        s = request.POST.get('subject')
        w = request.user.username
        c = request.POST.get('content')
        if s and c:
            Board(subject=s, writer=w, content=c).save()
        return redirect('board:index')
    return render(request, "bd/create.html")

def detail(request, num):
    b = Board.objects.get(id=num)
    r = b.reply_set.all()
    context={
        'con' : b,
        'rep' : r
    }
    return render(request, "bd/detail.html", context)

def delete(request, num):
    b = Board.objects.get(id=num)
    if request.user.username == b.writer:
        b.delete()
    else:
        return render(request, "error/forbidden.html")
    return redirect('board:index')

def update(request, num):
    b = Board.objects.get(id=num)
    if not(request.user.username == b.writer):
        return render(request, "error/forbidden.html")
    if request.method == "POST":
        s = request.POST.get('subject')
        c = request.POST.get('content')
        if s:
            b.subject = s
        b.content = c
        b.save()
        return redirect("board:detail", num=num)
    context = {
        'con' : b
    }
    return render(request, "bd/update.html", context)

def up(request, conid, st):
    b = Board.objects.get(id=conid)
    if (request.user.username):
        if st == 'down':
            b.up.remove(request.user)
        else:
            b.up.add(request.user)
    else:
        return redirect("acc:login")
    return redirect("board:detail", num=conid)

def create_reply(request, conid):
    b = Board.objects.get(id=conid)
    c = request.POST.get('comment')

    Reply(subject=b, comment=c, replyer=request.user.username, replyer_pic=request.user.pic).save()
    return redirect("board:detail", num=conid)

def rep_up(request, conid, num, st):
    b = Reply.objects.get(id=num)
    if (request.user.username):
        if st == 'down':
            b.agree.remove(request.user)
        else:
            b.agree.add(request.user)
    else:
        return redirect("acc:login")
    return redirect("board:detail", num=conid)