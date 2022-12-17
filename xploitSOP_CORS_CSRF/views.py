from django.shortcuts import render, redirect
import os
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

TEST_USERNAME = "test"
TEST_PASSWORD = "test"
RANDOM_SESSION_ID = "1337"
SESSION_COOKIE_NAME = "APP_SESSION_ID"


def index(request):
	

	if request.method == "POST":
		if request.POST.get("username") == TEST_USERNAME and request.POST.get("password") == TEST_PASSWORD:
			context = {'username': TEST_USERNAME}
			response = render(request, 'home_scc.html', context)
			response.set_cookie(SESSION_COOKIE_NAME, RANDOM_SESSION_ID, httponly=False, secure=False, samesite='none')  # Setting a static session cookie is Insecure!
			return response
	
	return render(request, 'index_scc.html')


@csrf_exempt
def run(request):

	if request.method == "OPTIONS":
		response = HttpResponse()
		response["Access-Control-Allow-Origin"] = request.headers.get("Origin")
		response["Access-Control-Allow-Headers"] = "content-type"
		response["Access-Control-Allow-methods"] = "POST"
		response["Access-Control-Allow-Credentials"] = "true"
		return response

	if request.method == "POST":
		if not isAuthenticated(request):
			return redirect("/xploitSCC")
		msg = ""		
		if request.content_type == "application/json":
			body = json.loads(request.body)
			os.system(body["instructions"])
			context = {"msg": "Instructions have been run"}
			response = render(request, 'run.html', context)
			response["Access-Control-Allow-Origin"] = request.headers.get("Origin")
			response["Access-Control-Allow-Headers"] = "content-type"
			response["Access-Control-Allow-methods"] = "POST"
			response["Access-Control-Allow-Credentials"] = "true"
			return response
		else:
			msg = "Invalid Content Type"
			return HttpResponse(msg)
	else:
		return HttpResponse("Only OPTIONS and POST methods are supported")



def isAuthenticated(request):
	if RANDOM_SESSION_ID == request.COOKIES.get(SESSION_COOKIE_NAME):
		return True
	return False


def chg_pwd_get(request):
	
	if not isAuthenticated(request):
		return redirect("/xploitSCC")

	if request.method == "GET":
		if request.GET.get("new_password"):

			# Imagin the actual Password Change code here
			print("The user password has been changed to %s" % request.GET.get("new_password"))

			return HttpResponse("Password changed!")
		else:
			return HttpResponse("Couldn't change the Password. The new_password parameter not supplied.")
	else:
		return HttpResponse("Only GET method is supported")

#@csrf_exempt
def chg_pwd_post(request):

	if not isAuthenticated(request):
		return redirect("/xploitSCC")

	if request.method == "POST":
		if request.POST.get("new_password"):

			# Imagin the actual Password Change code here
			print("The user password has been changed to %s" % request.POST.get("new_password"))

			return HttpResponse("Password changed!")
		else:
			return HttpResponse("Couldn't change the Password. The new_password parameter not supplied.")
	else:
		return HttpResponse("Only POST method is supported")


@csrf_exempt
def chg_pwd_json(request):

	if not isAuthenticated(request):
		return redirect("/xploitSCC")

	if request.method == "POST":
		if request.content_type == "application/json":
			body = json.loads(request.body)

			if body["new_password"]:

				# Imagin the actual Password Change code here
				print("The user password has been changed to %s" % request.POST.get("new_password"))

				return HttpResponse("Password changed!")
			else:
				return HttpResponse("Couldn't change the Password. The new_password parameter not supplied.")
		else:
				return HttpResponse("Unsupported Content-Type.")

	else:
		return HttpResponse("Only POST method is supported")



@csrf_exempt
def chg_pwd_std(request):

	if not isAuthenticated(request):
		return redirect("/xploitSCC")

	if request.method == "POST":
		
		# Imagin the actual Password Change code here
		print("The user password has been changed")

		return HttpResponse("Password changed!")

	else:
		return HttpResponse("Only POST method is supported")


@csrf_exempt
def chg_pwd_permissive_cors(request):

	if request.method == "OPTIONS":
		response = HttpResponse()
		response["Access-Control-Allow-Origin"] = request.headers.get("Origin")
		response["Access-Control-Allow-Headers"] = "content-type"
		response["Access-Control-Allow-methods"] = "POST"
		response["Access-Control-Allow-Credentials"] = "true"
		return response

	if request.method == "POST":
		if not isAuthenticated(request):
			return redirect("/xploitSCC")

		# Imagin the actual Password Change code here
		print("The user password has been changed")
		response = HttpResponse("Password changed!")
		response["Access-Control-Allow-Origin"] = request.headers.get("Origin")
		response["Access-Control-Allow-Headers"] = "content-type"
		response["Access-Control-Allow-methods"] = "POST"
		response["Access-Control-Allow-Credentials"] = "true"

		return response

	else:
		return HttpResponse("Only OPTIONS and POST methods are supported")


@csrf_exempt
def chg_pwd_wildcard(request):

	if request.method == "OPTIONS":
		response = HttpResponse()
		response["Access-Control-Allow-Origin"] = "*"
		response["Access-Control-Allow-Headers"] = "content-type"
		response["Access-Control-Allow-methods"] = "POST"
		# response["Access-Control-Allow-Credentials"] = "true"
		return response

	if request.method == "POST":
		if not isAuthenticated(request):
			return redirect("/xploitSCC")

		# Imagin the actual Password Change code here
		print("The user password has been changed")
		response = HttpResponse("Password changed!")
		response["Access-Control-Allow-Origin"] = "*"
		response["Access-Control-Allow-Headers"] = "content-type"
		response["Access-Control-Allow-methods"] = "POST"
		# response["Access-Control-Allow-Credentials"] = "true"

		return response

	else:
		return HttpResponse("Only OPTIONS and POST methods are supported")


@csrf_exempt
def chg_pwd_null_origin(request):

	if request.method == "OPTIONS":
		response = HttpResponse()
		response["Access-Control-Allow-Origin"] = "null"
		response["Access-Control-Allow-Headers"] = "content-type"
		response["Access-Control-Allow-methods"] = "POST"
		response["Access-Control-Allow-Credentials"] = "true"
		return response

	if request.method == "POST":
		if not isAuthenticated(request):
			return redirect("/xploitSCC")

		# Imagin the actual Password Change code here
		print("The user password has been changed")
		response = HttpResponse("Password changed!")
		response["Access-Control-Allow-Origin"] = "null"
		response["Access-Control-Allow-Headers"] = "content-type"
		response["Access-Control-Allow-methods"] = "POST"
		response["Access-Control-Allow-Credentials"] = "true"

		return response

	else:
		return HttpResponse("Only OPTIONS and POST methods are supported")


def my_balance_permissive_cors(request):

	if request.method == "GET":
		response = HttpResponse("<p>Bank Account Balance: 1337,1337")
		response["Access-Control-Allow-Origin"] = request.headers.get("Origin")
		response["Access-Control-Allow-Headers"] = "content-type"
		response["Access-Control-Allow-methods"] = "GET"
		response["Access-Control-Allow-Credentials"] = "true"
		return response
		

def my_balance_no_cors(request):
	if request.method == "GET":
		response = HttpResponse("<p>Bank Account Balance: 1337,1337")
		
		return response