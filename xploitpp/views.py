from django.shortcuts import render, redirect
import subprocess, json


def index(request):
    return render(request, 'ppindex.html')


def welcome(request):
    class User:
        def __init__(self):
            pass

    if request.method == "POST":
        user = User()
        name = json.loads(request.POST.get('json'))

        merge(name, user)
        subprocess.Popen('whoami', shell=True)

        context = {"user": user}
        return render(request, 'ppwelcome.html', context)

    return redirect('/xploitpp/')



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


