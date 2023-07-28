import json
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from IELTS_eLearning_frontend.localsettings import url
from django.contrib import messages
import requests

# Create your views here.
def home(request):
    # urls = f'{url}writing test'
    # response=requests.get(url=urls)
    # print(response.json())
    print(request.session.get('std_token'))
    return render(request, 'index.html',context={'title': 'Home'})

def register(request):
    if request.method == 'POST':
        identity = request.POST.get('identity')
        uname = request.POST.get('username')
        mail = request.POST.get('email')
        pwd = request.POST.get('password')
        confirm_pass = request.POST.get('conf-password')
        
        registerURL=""
        if identity == "student":
            registerURL = f'{url}register'
        else: 
            registerURL = f'{url}teacher/register'
        data = {
            "username": uname,
            "email": mail,
            "password": pwd
        }
        response = requests.post(url=registerURL, json=data)
        if response.status_code == 201:
            if pwd == confirm_pass:
                # request.session['reg_username']=uname
                messages.info(request, response.json()['msg'])
                return redirect("profile")
            else:
                messages.error(request, "Entered Password and Confirm Password Both are not same!")
        else:
            messages.info(request,response.json())
            return redirect('register')
    return render(request, 'register.html',context={'title': 'register'})

def login(request):
    if request.method == "POST":
        identity = request.POST.get('identity')
        username=request.POST['username']
        password=request.POST['password']
        login_url = ""
        if identity == "student":
            login_url = f'{url}login'
        else:
            login_url = f'{url}teacher/login'
        data = {
            "username": username,
            "password": password
        }
        response = requests.post(url=login_url, data=data)
        if response.status_code == 201:
            obj=response.json()
            print(obj)
            request.session['username'] = response.json()["username"]
            if identity == "student":
                request.session['std_user']= response.json()["username"]
                request.session['std_token'] = response.json()["token"]
            else:
                request.session['tcher_user']= response.json()["username"]
                request.session['tcher_token'] = response.json()["token"]
            messages.info(request, "Loged in successfully!")
            return redirect('home')
        else:
            messages.info(request, response.json()['msg'])
            return redirect("login")
    return render(request, 'login.html',context={'title': 'login'})

def logout(request):
    if 'username' in request.session.keys():
        urls = f'{url}logout'
        data = {
            "username": request.session['username']
        }
        response = requests.post(url=urls, json=data)
        if response.status_code == 200:
            if 'std_user' in request.session:
                if request.session['username'] == request.session['std_user']:
                    request.session.pop('std_user')
            if 'tcher_user' in request.session:
                if request.session['username'] == request.session['tcher_user']:
                    request.session.pop('tcher_user')
            request.session.pop('username')
            messages.info(request, "Logout successfully!")
        else:
            return HttpResponse("could not Logout", status=405)
    return redirect('login')

def profile(request):
    if 'reg_username' in request.session.keys() or 'username' in request.session.keys():
        if request.method == 'POST':
            user = ""
            if 'reg_username' in request.session.keys():
                user = request.session['reg_username']
            if 'username' in request.session.keys():
                user = request.session['username']
            user_type = request.POST.get('profile_option')
            fname = request.POST.get('fname')
            lname = request.POST.get('lname')
            country = request.POST.get('country')
            urls = f'{url}profile'
            data = {
                "user": user,
                "type_of_user": user_type,
                "first_name": fname,
                "last_name": lname,
                "country": country
            }
            response = requests.post(url=urls, json=data)
            if response.status_code==201:
                messages.info(request, response.json()['msg'])
                request.session.pop('reg_username')
                return redirect("login")
            else:
                messages.info(request, response.json())
                return redirect('profile')
    return render(request, 'profile.html',context={'title': 'profile'})

def examLibrary(request):
    if request.method == 'POST':
        option = request.POST.get('profile_option')
        request.session['profile_option'] = option
        if 'tcher_user' in request.session.keys():
            if option == 'writing':
                # return render(request, "../../teacher_app/templates/writingTest.html", {'option': option})
                return HttpResponseRedirect('teacher/writingTest')
            if option == 'listening':
                return HttpResponseRedirect('teacher/listeningTest')
            if option =='speaking':
                return HttpResponseRedirect('teacher/speakingTest')
            if option == 'reading':
                return HttpResponseRedirect('teacher/readingTest')
            # return redirect('post_questions')
        else:
            pass
        
        # return render(request, 'addQuestion.html', {'option': option})
    return render(request, 'examLibrary.html',context={'title': 'examLibrary'})

def courses(request):
    return render(request, 'courses.html',context={'title': 'course'})

def about(request):
    return render(request, 'about.html',context={'title': 'about'})

def contact(request):
    return render(request, 'contact.html',context={'title': 'contact'})

def team (request):
    return render(request, 'team.html',context={'title': 'team'})

def testimonial(request):
    return render(request, 'testimonial.html',context={'title': 'testimonial'})

def four04(request):
    return render(request, '404.html',context={'title': '404'})

def myTests(request):
    print(request.session.get('token'))
    urls = f'{url}student-myTests-writingTest'
    # header={'token': request.session.get('token')}
    # response = requests.request("GET",url=urls, headers=header)
    # print(response.json())
    
    # url = "http://127.0.0.1:8000/student-myTests-writingTest"

    payload = {}
    headers = {'token': str(request.session.get('std_token'))}

    response = requests.request("GET", urls, headers=headers, data=payload)
    data=json.loads(response.text)
    print(data)
    return render(request,'myTests.html',context={'title':'myTests','records':json.dumps(data)})