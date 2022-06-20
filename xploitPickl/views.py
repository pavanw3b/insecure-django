from django.shortcuts import render, redirect
import traceback
import pickle
from base64 import b64encode, b64decode


def index(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")

        # user = User(first_name=first_name, last_name=last_name)
        user = {"first_name": first_name, "last_name": last_name}
        response = redirect('/xploitpickl/dashboard')
        user_encoded = b64encode(pickle.dumps(user))
        user_encoded = user_encoded.decode("utf-8")  # For byte to string
        response.set_cookie('user', user_encoded)
        return response

    return render(request, 'index.html')


def dashboard(request):
    try:
        if request.COOKIES.get('user'):
            user_cookie = request.COOKIES.get('user')
            print("Cookie: %s" % user_cookie)
            user_cookie = b64decode(user_cookie)
            user = pickle.loads(user_cookie, encoding='utf-8')
            context = {"app_user": user}
            return render(request, 'dashboard.html', context)
        else:
            return redirect("/")
    except KeyError:
        print("Key error")
        return redirect("/")

    except ValueError:
        print("Val error")
        return redirect("/")

    except Exception as e:
        print("%s \n %s " % (str(e), traceback.format_exc()))
        return redirect("/")
