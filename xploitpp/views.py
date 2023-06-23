from django.shortcuts import render
import subprocess

def index(request):
	return render(request, 'ppindex.html')


def welcome(request):
    class Employee:
        def __init__(self):
            pass


    if request.method == "POST":
        name = request.POST.get("name")

        context = {"name": name}
        return render(request, 'ppwelcome.html', context)

    return render(request, 'index.html')


def merge(src, dst):
    # Recursive merge function
    for k, v in src.items():
        if hasattr(dst, '__getitem__'):
            if dst.get(k) and type(v) == dict:
                merge(v, dst.get(k))
            else:
                dst[k] = v
        elif hasattr(dst, k) and type(v) == dict:
            merge(v, getattr(dst, k))
        else:
            setattr(dst, k, v)


