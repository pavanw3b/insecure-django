from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from django.http import JsonResponse
import pycurl
from io import BytesIO
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return render(request, 'xploitSSRF/index.html')


def import_url(request):
    url = request.POST.get("profile_url")
    
    b = BytesIO()
    crl = pycurl.Curl()
    crl.setopt(crl.URL, url)
    crl.setopt(crl.WRITEFUNCTION, b.write)
    crl.perform()
    crl.close()
    response = b.getvalue().decode('UTF-8')
    soup = BeautifulSoup(response, 'html.parser')
    try:
        name = (soup.find_all("h1", {"class": "name"})[0].text.strip())
        if name:    
            context = {'visitor_name': name }
            return render(request, 'xploitSSRF/homepage.html', context)
        else:
            context = {'status': 'error', 'response': response}
    except:
        context = {'status': 'error', 'response': response}

    return render(request, 'xploitSSRF/index.html', context)


def api_documentation(request):
    if "127.0.0.1" == request.META['REMOTE_ADDR']:
        return JsonResponse({
            'name': 'API Documentation',
            'items': {
                'item1': {
                    'name': 'Get API Token',
                    'url': 'xploitSSRF/api/token',
                    'method': 'GET',
                    'parameters': 'none'
                },
                'item2': {
                    'name': 'Reset Admin    password to default',
                    'url': 'xploitSSRF/api/admin/reset',
                    'method': 'POST',
                    'parameters': 'user_id'
                }
            }
        })
    return JsonResponse({"response": "Unauthorized access"})

@csrf_exempt
def api_admin_password_reset(request):

    if "127.0.0.1" != request.META['REMOTE_ADDR']:
        return JsonResponse({"response": "Unauthorized access"})
    if "POST" != request.method:
        return JsonResponse({"response": "Method not supported"})
    if "" == request.POST.get("user_id"):
        return JsonResponse({"response": "Missing user_id"})
    user_id = request.POST.get("user_id")
    # @TODO Demo. Implement actual password change the default.
    return JsonResponse({"response": "The password of %s has been reset to %s" % (user_id, user_id)})



@csrf_exempt
def api_token(request):

    if "127.0.0.1" != request.META['REMOTE_ADDR']:
        return JsonResponse({"response": "Unauthorized access"})
    if "GET" != request.method:
        return JsonResponse({"response": "Method not supported"})

    
    return JsonResponse({"token": "u4PHVXvAzhF5TA6stkbWFkFviKVMsJxc9"})