from django.shortcuts import render, redirect
import os
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')


def run(request):
    if request.method == "POST":
        if request.POST.get('instructions'):
            os.system(request.POST.get('instructions'))
    else:
        if request.GET.get('instructions'):
            os.system(request.GET.get('instructions'))
        html = "<html><body>Called in GET</body></html>"
        return HttpResponse(html)
