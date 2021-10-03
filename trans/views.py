from django.shortcuts import render
from googletrans import Translator

# Create your views here.
def index(request):
    if request.method == "POST":
        i = request.POST.get("input")
        f = request.POST.get('from')
        t = request.POST.get('to')
        if i:
            translator = Translator()
            o = translator.translate(i, src=f, dest=t)
            re = {
                'in' : i,
                'out' : o.text,
                'from' : f,
                'to' : t,
            }
            return render(request, 'trans/index.html', re)
    return render(request, 'trans/index.html')