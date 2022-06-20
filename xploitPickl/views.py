from django.shortcuts import render, redirect
from .models import User
import pickle
from base64 import b64encode, b64decode


def index(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")

        user = User(first_name=first_name, last_name=last_name)
        response = redirect('/xploitpickl/dashboard')
        response.set_cookie('user', b64encode(pickle.dumps(user)).decode("utf-8"))
        return response

    return render(request, 'index.html')


def dashboard(request):
    try:
        if request.COOKIES.get('user'):
            user_cookie = request.COOKIES.get('user')
            user = pickle.loads(b64decode(user_cookie))
            context = {"app_user": user}
            render(request, 'dashboard.html', context)
        else:
            redirect("/")
    except KeyError:
        redirect("/")
    except ValueError:
        redirect("/")
    except Exception:
        redirect("/")
