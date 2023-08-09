import json
from django.http import JsonResponse
from django.shortcuts import render, redirect
from IELTS_eLearning_frontend.localsettings import url
from django.contrib import messages
import requests

def teacherWritingTest(request):
    if request.method == 'POST':
        tcher = request.session['tcher_user']
        content1 = request.POST.get('content1')
        image = request.FILES.get('image')
        content2 = request.POST.get('content2')

        urls = f'{url}teacher/writingTests'
        headers = {
            "token": request.session['tcher_token']
        }
        data = {
            "teacher": tcher,
            "content1": content1,
            "content2": content2,
        }
        file = {
            'image': image
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
        print(tcher)
        audio = request.FILES.get('audio_file')
        urls = f'{url}teacher/listeningTests'
        headers = {
            "token": request.session['tcher_token']
        }
        data = {
            "teacher": tcher
            # "question": audio,
        }
        file = {
            'question': audio
        }
        response = requests.post(url=urls, data=data, files=file, headers=headers)
        if response.status_code == 201:
            messages.success(request, {'msg': 'Question added successfully!', 'status': 'success'})
            return redirect('listeningTest')
        else:
            messages.error(request, {'msg': 'Something went wrong!', 'status': 'error'})
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
        if response.status_code == 201:
            messages.success(request, {'msg': 'Question added successfully!', 'status': 'success'})
            return redirect('speakingTest')
        else:
            messages.error(request, {'msg': 'Something went wrong!', 'status': 'error'})
            return redirect('speakingTest')
    return render(request,'speakingTest.html')

def teacherReadingTest(request):
    if request.method == 'POST':
        tcher = request.session['tcher_user']
        question = request.POST.get('content')
            
        subQuestionsList = request.POST.getlist('ques')
        answerList = request.POST.getlist('ans')
        subQuestions =[]
        rightAnswers = []
        for key,value in enumerate(subQuestionsList, 1):
            tempData ={"Q"+str(key): value}
            subQuestions.append(tempData)

        for key,value in enumerate(answerList, 1):
            tempData ={"ans"+str(key): value}
            rightAnswers.append(tempData)  
        urls = f'{url}teacher/readingTests'
        headers = {
            "token": request.session['tcher_token']
        }
        data = {
            "teacher": tcher,
            "question": question,
            "subQuestion": subQuestions,
            "rightAnswers": rightAnswers
        }
        response = requests.post(url = urls,json=data, headers = headers)
        if response.status_code == 201:
            messages.success(request, {'msg': 'Question added successfully!', 'status': 'success'})
            return redirect('readingTest')
        else:
            messages.error(request, {'msg': 'Something went wrong!', 'status': 'error'})
            return redirect('readingTest')
    return render(request, 'readingTest.html')

def editWritingQuestion(request):
    return render(request, 'editWritingQuestion.html')

def editReadingQuestion(request):
    return render(request, 'editReadingQuestion.html')

def editListeningQuestion(request):
    return render(request, 'editListingQuestion.html')

def editSpeakerQuestion(request):
    return render(request, 'editSpeakingQuestion.html')
    
def deleteWritingQuestion(request):
    if request.method == 'POST' :
        urls = f'{url}teacher/writingTests'
        return deleteQuestion(request,urls)
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
        headers={'token': request.session.get('tcher_token')}
        response = requests.get(url=urls,headers=headers)
        if response.status_code == 201:
            writingQuestions = response.json()
        else:
            writingQuestions = []
        
        urls = f'{url}teacher/ListeningQuestionListView'
        response = requests.get(url=urls,headers=headers)
        if response.status_code == 201:
            listeningQuestions = response.json()
        else:
            listeningQuestions = []
        
        urls = f'{url}teacher/ReadingQuestionListView'
        response = requests.get(url=urls,headers=headers)
        if response.status_code == 201:
            readingQuestions = response.json()
        else: 
            readingQuestions = []
        
        urls = f'{url}teacher/SpeakingQuestionListView'
        response = requests.get(url=urls,headers=headers)
        if response.status_code == 201:
            speakingQuestions = response.json()
        else:
            speakingQuestions = []
        # speakingQuestions[0]['question'] = speakingQuestions[0]['question'].replace('”',"'").replace('“',"'")
        
        return render(request,'myQuestions.html', {'writingQuestions': writingQuestions,'listeningQuestions':listeningQuestions,'readingQuestions':readingQuestions,'speakingQuestions':speakingQuestions})


####################################################
### send request to server for deleting questions###
####################################################

def deleteQuestion(request,urls):
    question_id = request.POST.get('id')
    headers = {
        "token": request.session['tcher_token']
    }
    data = {
        "question_id": question_id,
    }
    response = requests.delete(url=urls, data=data, headers=headers)
    return JsonResponse({'msg': response.json()})

###################################################