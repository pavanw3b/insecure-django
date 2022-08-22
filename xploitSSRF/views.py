from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from django.http import JsonResponse


def index(request):
    return render(request, 'xploitSSRF/index.html')


def import_linkedin_url(request):
    url = request.POST.get("li_url")
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    # @TODO: Implement a real parsing using linkedin publi profile soup finding
    context = {'li_response_body': soup.get_text()}
    return render(request, 'xploitSSRF/index.html', context)


def api_documentation(request):
    if "127.0.0.1" == request.META['REMOTE_ADDR']:
        return JsonResponse({
            'name': 'API Documentation',
            'items': {
                'item1': {
                    'name': 'Get API Token',
                    'url': 'xploissrf/api/token',
                    'method': 'GET',
                    'parameters': 'none'
                },
                'item2': {
                    'name': 'Reset Admin    password to default',
                    'url': 'xploissrf/api/admin/reset',
                    'method': 'POST',
                    'parameters': 'user_id'
                }
            }
        })
    return JsonResponse({"response": "Unauthorized access"})


def api_admin_password_reset(request):
    if "127.0.0.1" != request.META['REMOTE_ADDR']:
        return JsonResponse({"response": "Unauthorized access"})
    if "POST" != request.method:
        return JsonResponse({"response": "Method not supported"})
    if "" != request.POST.get("user_id"):
        return JsonResponse({"response": "Missing user_id"})
    user_id = request.POST.get("user_id")
    # @TODO Demo. Implement actual password change the default.
    return JsonResponse({"response": "The password has been reset %s" % user_id})
