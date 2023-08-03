import json
from django.http import JsonResponse
from django.shortcuts import render, redirect
from IELTS_eLearning_frontend.localsettings import url
from django.contrib import messages
import requests

def teacherWritingTest(request):
    if request.method == 'POST':
        tcher = request.session['tcher_user']
        content = request.POST.get('content')
        images = request.FILES.get('images')
        urls = f'{url}teacher/writingTests'
        headers = {
            "token": request.session['tcher_token']
        }
        data = {
            "teacher": tcher,
            "content": content,
            # "images": images,
        }
        file = {
            'images': images
        }
        response = requests.post(url=urls, data=data, files=file, headers=headers)
        if response.status_code == 201:
            messages.success(request, {'msg': 'Question added successfully!','status': 'success'})
            return redirect('writingTest')
        else:
            messages.error(request, {'msg': 'Something went wrong!','status': 'error'})
            return redirect('writingTest')
    return render(request, 'writingTest.html')

def teacherListeningTest(request):
    if request.method == 'POST':
        tcher = request.session['tcher_user']
        audio = request.FILES.get('audio_file')
        urls = f'{url}teacher/listeningTests'
        headers = {
            "token": request.session['tcher_token']
        }
        data = {
            "teacher": tcher,
            # "question": audio,
        }
        file = {
            'question': audio
        }
        response = requests.post(url=urls, data=data, files=file, headers=headers)
        if response.status_code == 201:
            messages.success(request, {'msg': 'Question added successfully!'})
            return redirect('listeningTest')
        else:
            messages.error(request, {'msg': 'Something went wrong!'})
            return redirect('listeningTest')
    return render(request, 'listeningTest.html')

def teacherSpeakingTest(request):
    if request.method == 'POST':
        tcher = request.session['tcher_user']
        topic = request.POST.get('content')
        urls = f'{url}teacher/speakingTests'
        headers = {
            "token": request.session['tcher_token']
        }
        data = {
            "teacher": tcher,
            "question": topic,
        }
        response = requests.post(url=urls, data=data, headers=headers)
        print("response: ", response.status_code)
        if response.status_code == 201:
            messages.success(request, {'msg': 'Question added successfully!'})
            return redirect('speakingTest')
        else:
            messages.error(request, {'msg': 'Something went wrong!'})
            return redirect('speakingTest')
    return render(request,'speakingTest.html')

def teacherReadingTest(request):
    if request.method == 'POST':
        tcher = request.session['tcher_user']
        question = request.POST.get('content')
        subQuestionsList = request.POST.getlist('ques')
        subQuestions =[]
        for key,value in enumerate(subQuestionsList, 1):
            tempData ={"Q"+str(key):value}
            subQuestions.append(tempData)
            
        urls = f'{url}teacher/readingTests'
        headers = {
            "token": request.session['tcher_token']
        }
        data = {
            "teacher": tcher,
            "question": question,
            "subQuestion": subQuestions,
        }
        response = requests.post(url = urls,json=data, headers = headers)
        if response.status_code == 201:
            messages.success(request, {'msg': 'Question added successfully!', 'status': 'success'})
            return redirect('readingTest')
        else:
            messages.error(request, {'msg': 'Something went wrong!', 'status': 'error'})
            return redirect('readingTest')
    return render(request, 'readingTest.html')

def checkWritingTest(request):
    if request.method == 'GET':
        tcher = request.session['tcher_user']
        urls = f'{url}teacher/checkWritingTest'
        data = {
            "teacher": tcher,
        }
        headers={'token': request.session.get('tcher_token'),}
        response = requests.get(url=urls, data=data,headers=headers)
        if response.status_code == 200:
            return render(request, 'checkWritingTest.html', {'response': response.json()})
        else:
            return render(request, 'checkWritingTest.html', {'response': response.json()})
        
def myQuestions(request):
    if request.method == 'GET':
        urls = f'{url}teacher/WritingQuestionsListView'
        headers={'token': request.session.get('tcher_token'),}
        response = requests.get(url=urls,headers=headers)
        writingQuestions = response
        
        urls = f'{url}teacher/ListeningQuestionListView'
        response = requests.get(url=urls,headers=headers)
        listeningQuestions = response
        
        urls = f'{url}teacher/ReadingQuestionListView'
        headers={'token': request.session.get('tcher_token'),}
        response = requests.get(url=urls,headers=headers)
        readingQuestions = response
        
        urls = f'{url}teacher/SpeakingQuestionListView'
        headers={'token': request.session.get('tcher_token'),}
        response = requests.get(url=urls,headers=headers)
        speakingQuestions = response
        # speakingQuestions[0]['question'] = speakingQuestions[0]['question'].replace('”',"'").replace('“',"'")
        
        if response.status_code == 201:
            return render(request,'myQuestions.html', {'writingQuestions': writingQuestions.json(),'listeningQuestions':listeningQuestions.json(),'readingQuestions':readingQuestions.json(),'speakingQuestions':speakingQuestions.text.replace('”',"'").replace('“',"'").replace('"',"'")})
        else:
            return render(request,'myQuestions.html', {'writingQuestions': writingQuestions.json()})

def deleteWritingQuestion(request):
    if request.method == 'POST' :
        print(request.POST)
        question_id = request.POST.get('id')
        print(question_id)
        urls = f'{url}teacher/writingTests'
        headers = {
            "token": request.session['tcher_token']
        }
        data = {
            "question_id": question_id,
        }
        response = requests.delete(url=urls, data=data, headers=headers)
        return JsonResponse({'msg': response.json()})
    else:
        return JsonResponse({'msg': 'Something went wrong', 'status': 'error'  })
    
def deleteReadingQuestion(request):
    if request.method == 'POST' :
        urls = f'{url}teacher/readingTests'
        return deleteQuestion(request,urls)
    else:
        return JsonResponse({'msg': 'Something went wrong', 'status': 'error'  })
    
def deleteListeningQuestion(request):
    if request.method == 'POST' :
        urls = f'{url}teacher/listeningTests'
        return deleteQuestion(request,urls)
    else:
        return JsonResponse({'msg': 'Something went wrong','status': 'error'  })
    
def deleteSpeakingQuestion(request):
    if request.method == 'POST' :
        urls = f'{url}teacher/speakingTests'
        return deleteQuestion(request,urls)
    else:
        return JsonResponse({'msg': 'Something went wrong','status': 'error'  })

####################################################
### send request to server for deleting questions###
####################################################

def deleteQuestion(request,urls):
    print(request.POST)
    question_id = request.POST.get('id')
    print(question_id)
    headers = {
        "token": request.session['tcher_token']
    }
    data = {
        "question_id": question_id,
    }
    response = requests.delete(url=urls, data=data, headers=headers)
    return JsonResponse({'msg': response.json()})

###################################################