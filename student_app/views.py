import json
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from IELTS_eLearning_frontend.localsettings import url, media_url
from django.contrib import messages
import requests
countries=[('AF','Afghanistan'), ('AL','Albania'), ('DZ','Algeria'), ('AS','American Samoa'), ('AD','Andorra'), ('AO','Angola'), ('AI','Anguilla'), ('AQ','Antarctica'), ('AG','Antigua And Barbuda'), ('AR','Argentina'), ('AM','Armenia'), ('AW','Aruba'), ('AU','Australia'), ('AT','Austria'), ('AZ','Azerbaijan'), ('BS','Bahamas'), ('BH','Bahrain'), ('BD','Bangladesh'), ('BB','Barbados'), ('BY','Belarus'), ('BE','Belgium'), ('BZ','Belize'), ('BJ','Benin'), ('BM','Bermuda'), ('BT','Bhutan'), ('BO','Bolivia'), ('BA','Bosnia And Herzegovina'), ('BW','Botswana'), ('BV','Bouvet Island'), ('BR','Brazil'), ('IO','British Indian Ocean Territory'), ('BN','Brunei Darussalam'), ('BG','Bulgaria'), ('BF','Burkina Faso'), ('BI','Burundi'), ('KH','Cambodia'), ('CM','Cameroon'), ('CA','Canada'), ('CV','Cape Verde'), ('KY','Cayman Islands'), ('CF','Central African Republic'), ('TD','Chad'), ('CL','Chile'), ('CN','China'), ('CX','Christmas Island'), ('CC','Cocos (keeling) Islands'), ('CO','Colombia'), ('KM','Comoros'), ('CG','Congo'), ('CD','Congo, The Democratic Republic Of The'), ('CK','Cook Islands'), ('CR','Costa Rica'), ('CI','Cote Divoire'), ('HR','Croatia'), ('CU','Cuba'), ('CY','Cyprus'), ('CZ','Czech Republic'), ('DK','Denmark'), ('DJ','Djibouti'), ('DM','Dominica'), ('DO','Dominican Republic'), ('TP','East Timor'), ('EC','Ecuador'), ('EG','Egypt'), ('SV','El Salvador'), ('GQ','Equatorial Guinea'), ('ER','Eritrea'), ('EE','Estonia'), ('ET','Ethiopia'), ('FK','Falkland Islands (malvinas)'), ('FO','Faroe Islands'), ('FJ','Fiji'), ('FI','Finland'), ('FR','France'), ('GF','French Guiana'), ('PF','French Polynesia'), ('TF','French Southern Territories'), ('GA','Gabon'), ('GM','Gambia'), ('GE','Georgia'), ('DE','Germany'), ('GH','Ghana'), ('GI','Gibraltar'), ('GR','Greece'), ('GL','Greenland'), ('GD','Grenada'), ('GP','Guadeloupe'), ('GU','Guam'), ('GT','Guatemala'), ('GN','Guinea'), ('GW','Guinea-bissau'), ('GY','Guyana'), ('HT','Haiti'), ('HM','Heard Island And Mcdonald Islands'), ('VA','Holy See (vatican City State)'), ('HN','Honduras'), ('HK','Hong Kong'), ('HU','Hungary'), ('IS','Iceland'), ('IN','India'), ('ID','Indonesia'), ('IR','Iran, Islamic Republic Of'), ('IQ','Iraq'), ('IE','Ireland'), ('IL','Israel'), ('IT','Italy'), ('JM','Jamaica'), ('JP','Japan'), ('JO','Jordan'), ('KZ','Kazakstan'), ('KE','Kenya'), ('KI','Kiribati'), ('KP','Korea, Democratic Peoples Republic Of'), ('KR','Korea, Republic Of'), ('KV','Kosovo'), ('KW','Kuwait'), ('KG','Kyrgyzstan'), ('LA','Lao Peoples Democratic Republic'), ('LV','Latvia'), ('LB','Lebanon'), ('LS','Lesotho'), ('LR','Liberia'), ('LY','Libyan Arab Jamahiriya'), ('LI','Liechtenstein'), ('LT','Lithuania'), ('LU','Luxembourg'), ('MO','Macau'), ('MK','Macedonia, The Former Yugoslav Republic Of'), ('MG','Madagascar'), ('MW','Malawi'), ('MY','Malaysia'), ('MV','Maldives'), ('ML','Mali'), ('MT','Malta'), ('MH','Marshall Islands'), ('MQ','Martinique'), ('MR','Mauritania'), ('MU','Mauritius'), ('YT','Mayotte'), ('MX','Mexico'), ('FM','Micronesia, Federated States Of'), ('MD','Moldova, Republic Of'), ('MC','Monaco'), ('MN','Mongolia'), ('MS','Montserrat'), ('ME','Montenegro'), ('MA','Morocco'), ('MZ','Mozambique'), ('MM','Myanmar'), ('NA','Namibia'), ('NR','Nauru'), ('NP','Nepal'), ('NL','Netherlands'), ('AN','Netherlands Antilles'), ('NC','New Caledonia'), ('NZ','New Zealand'), ('NI','Nicaragua'), ('NE','Niger'), ('NG','Nigeria'), ('NU','Niue'), ('NF','Norfolk Island'), ('MP','Northern Mariana Islands'), ('NO','Norway'), ('OM','Oman'), ('PK','Pakistan'), ('PW','Palau'), ('PS','Palestinian Territory, Occupied'), ('PA','Panama'), ('PG','Papua New Guinea'), ('PY','Paraguay'), ('PE','Peru'), ('PH','Philippines'), ('PN','Pitcairn'), ('PL','Poland'), ('PT','Portugal'), ('PR','Puerto Rico'), ('QA','Qatar'), ('RE','Reunion'), ('RO','Romania'), ('RU','Russian Federation'), ('RW','Rwanda'), ('SH','Saint Helena'), ('KN','Saint Kitts And Nevis'), ('LC','Saint Lucia'), ('PM','Saint Pierre And Miquelon'), ('VC','Saint Vincent And The Grenadines'), ('WS','Samoa'), ('SM','San Marino'), ('ST','Sao Tome And Principe'), ('SA','Saudi Arabia'), ('SN','Senegal'), ('RS','Serbia'), ('SC','Seychelles'), ('SL','Sierra Leone'), ('SG','Singapore'), ('SK','Slovakia'), ('SI','Slovenia'), ('SB','Solomon Islands'), ('SO','Somalia'), ('ZA','South Africa'), ('GS','South Georgia And The South Sandwich Islands'), ('ES','Spain'), ('LK','Sri Lanka'), ('SD','Sudan'), ('SR','Suriname'), ('SJ','Svalbard And Jan Mayen'), ('SZ','Swaziland'), ('SE','Sweden'), ('CH','Switzerland'), ('SY','Syrian Arab Republic'), ('TW','Taiwan, Province Of China'), ('TJ','Tajikistan'), ('TZ','Tanzania, United Republic Of'), ('TH','Thailand'), ('TG','Togo'), ('TK','Tokelau'), ('TO','Tonga'), ('TT','Trinidad And Tobago'), ('TN','Tunisia'), ('TR','Turkey'), ('TM','Turkmenistan'), ('TC','Turks And Caicos Islands'), ('TV','Tuvalu'), ('UG','Uganda'), ('UA','Ukraine'), ('AE','United Arab Emirates'), ('GB','United Kingdom'), ('US','United States'), ('UM','United States Minor Outlying Islands'), ('UY','Uruguay'), ('UZ','Uzbekistan'), ('VU','Vanuatu'), ('VE','Venezuela'), ('VN','Viet Nam'), ('VG','Virgin Islands, British'), ('VI','Virgin Islands, U.s.'), ('WF','Wallis And Futuna'), ('EH','Western Sahara'), ('YE','Yemen'), ('ZM','Zambia'), ('ZW','Zimbabwe')]
# Create your views here.
def home(request):
    urls = f'{url}writing test'
    response=requests.get(url=urls)
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
                messages.info(request, response.json())
                return redirect("login")
            else:
                messages.error(request,{"msg":"Entered Password and Confirm Password Both are not same!",'status':'success'})
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
            request.session['username'] = response.json()["username"]
            if identity == "student":
                request.session['std_user'] = response.json()["username"]
                request.session['std_token'] = response.json()["token"]
            else:
                request.session['tcher_user'] = response.json()["username"]
                request.session['tcher_token'] = response.json()["token"]
            messages.info(request,{'msg': "Logged in successfully!",'status':'success'})
            return redirect('home')
        else:
            messages.info(request, response.json())
            return redirect("login")
    return render(request, 'login.html', context={'title': 'login'})

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
            messages.info(request,{'msg': "Logout successfully!",'status':'success'})
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
    return render(request, 'profile.html',context={'title': 'profile','countries': countries})

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
        elif 'std_user' in request.session.keys():
            if option == 'writing':
                return redirect('writing_test')
            if option == 'listening':
                return redirect('listening_test')
            if option =='speaking':
                return redirect('speaking_test')
            if option =='reading':
                return redirect('reading_test')
        else:
            pass
        # return render(request, 'addQuestion.html', {'option': option})
    return render(request, 'examLibrary.html',context={'title': 'examLibrary'})

def writingTest(request):
    if 'std_user' in request.session.keys():
        urls = f'{url}writing-test'
        headers = {
            'token': request.session['std_token'],
        }
        if request.method == 'POST':
            que = request.POST.get('que_id')
            ans1= request.POST.get('answer1')
            ans2= request.POST.get('answer2')
            if str(ans1).strip() == "":
                ans1 = "None"
            if str(ans2).strip() == "":
                ans2 = "None"
            payload = { 
                    'question': que,
                    'answer1': ans1,
                    'answer2': ans2,
                }
            response = requests.request("POST", urls, headers=headers, data=payload)
            if response.status_code == 201:
                messages.success(request, {'msg': "Answer was submitted successfully!", 'status': 'success'})
                return redirect('examLibrary')
            else:
                messages.error(request, {'msg': "Answer submission failed!", 'status': 'error'})
                return redirect('writing_test')
       
        # to handle GET request
        response = requests.request("GET", urls, headers=headers)
        if response.status_code == 200:
            data = response.json()
            return render(request, 'std_writingTest.html', {"data": data, "media_url": media_url})
        else:
            return render(request, 'std_writingTest.html') 
    else:
        messages.info(request, {"msg": "You cannot open this page!", 'status': 'warning'})
        return redirect('examLibrary')

def listeningTest(request):
    if 'std_user' in request.session.keys():
        urls = f'{url}listing-test'
        headers = {
            'token': request.session['std_token'],
        }
        if request.method == 'POST':
            que = request.POST.get('que_id')
            ans = request.POST.get('answer')
            if str(ans).strip() == "":
                ans = "None"
            payload = {'question': que,
                        'answer': ans
                    }
            response = requests.request("POST", urls, headers=headers, data=payload)
            if response.status_code == 201:
                messages.success(request, {'msg': "Answer was submitted successfully!", 'status': 'success'})
                return redirect('examLibrary')
            else:
                messages.error(request, {'msg': "Answer submission failed!", 'status': 'error'})
                return redirect('listening_test')
        
        response = requests.request("GET", urls, headers=headers)
        if response.status_code == 200:
            data = response.json()
            audio = data[0]['question']
            return render(request, 'std_listeningTest.html', {"data": data, "media_url": audio})
        else:
            return render(request, 'std_listeningTest.html')
    else:
        messages.info(request, {"msg": "You cannot open this page!", 'status': 'warning'})
        return redirect('examLibrary')

def speakingTest(request): 
    if 'std_user' in request.session.keys():
        urls = f'{url}speaking-test'
        headers = {
            'token': request.session['std_token'],
        }
        if request.method == 'POST':
            que = request.POST.get('que_id')
            ans = request.FILES.get('audio_file')
            if str(ans).strip() == "":
                ans = "None"
            payload = {
                'question': que
            }
            files = {
                'answer': ans
            }
            response = requests.request("POST", urls, headers=headers, data=payload, files=files)
            if response.status_code == 201:
                messages.success(request, {'msg': "Answer was submitted successfully!", 'status': 'success'})
                return redirect('examLibrary')
            else:
                messages.error(request, {'msg': "Answer submission failed!", 'status': 'error'})
                return redirect('speaking_test')
        
        response = requests.request("GET", urls, headers=headers)
        if response.status_code == 200:
            data = response.json()
            return render(request, 'std_speakingTest.html', {"data": data})
        else:
            return render(request, 'std_speakingTest.html')
    else:
        messages.info(request, {"msg": "You cannot open this page!", 'status': 'warning'})
        return redirect('examLibrary')

def readingTest(request):
    if 'std_user' in request.session.keys():
        urls = f'{url}reading-test'
        headers = {
            'token': request.session['std_token'],
        }
        if request.method == 'POST':
            response = requests.request("POST", urls, headers=headers, data=json.dumps(request.POST))
            if response.status_code == 201:
                messages.success(request, {'msg': "Answer was submitted successfully!", 'status': 'success'})
                return redirect('examLibrary')
            else:
                messages.error(request, {'msg': "Answer submission failed!", 'status': 'error'})
                return redirect('reading_test')
        
        response = requests.request("GET", urls, headers=headers)
        if response.status_code == 200:
            data = response.json()
            return render(request, 'std_readingTest.html', {"data": data})
        else:
            return render(request, 'std_readingTest.html')
    else:
        messages.info(request, {"msg": "You cannot open this page!", 'status': 'warning'})
        return redirect('examLibrary')

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
    headers = {'token': str(request.session.get('std_token'))}
    
    urls = f'{url}student-myTests-writingTest'
    response = requests.request("GET", urls, headers=headers)
    writingTestData = json.loads(response.text)
    
    urls = f'{url}student-myTests-listeningTest'
    response = requests.request("GET", urls, headers=headers)
    
    listeningTestData = json.loads(response.text)
    
    urls = f'{url}student-myTests-readingTest'
    response = requests.request("GET", urls, headers=headers)
    readingTestData=json.loads(response.text)
    
    urls = f'{url}student-myTests-speakingTest'
    response = requests.request("GET", urls, headers=headers)
    speakingTestData=json.loads(response.text)
    
    return render(request, 'myTests.html', context={'title': 'myTests', 'writingTestData': json.dumps(writingTestData),'listeningTestData':json.dumps(listeningTestData),'readingTestData':json.dumps(readingTestData),'speakingTestData':json.dumps(speakingTestData)})