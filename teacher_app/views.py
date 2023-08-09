import json
from django.http import JsonResponse
from django.shortcuts import render, redirect
from IELTS_eLearning_frontend.localsettings import url
from django.contrib import messages
import requests

######################
### POST Questions ###
######################

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
        subQuestions =[]
        for key,value in enumerate(subQuestionsList, 1):
            tempData ={"Q"+str(key):value}
            subQuestions.append(tempData)
            
        subQuestionsList = request.POST.getlist('ques')
        subQuestions =[]
        rightAnswers = []
        for key,value in enumerate(subQuestionsList, 1):
            tempData ={"Q"+str(key): value}
            subQuestions.append(tempData)
            
        subQuestionsList = request.POST.getlist('ques')
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
        response = requests.post(url = urls,json=data, headers = headers)
        if response.status_code == 201:
            messages.success(request, {'msg': 'Question added successfully!', 'status': 'success'})
            messages.success(request, {'msg': 'Question added successfully!', 'status': 'success'})
            return redirect('readingTest')
        else:
            messages.error(request, {'msg': 'Something went wrong!', 'status': 'error'})
            messages.error(request, {'msg': 'Something went wrong!', 'status': 'error'})
            return redirect('readingTest')
    return render(request, 'readingTest.html')

######################
### edit Questions ###
######################

def editWritingQuestion(request,id):
    urls = f'{url}teacher/writingTests'
    if request.method == 'POST':
        tcher = request.session['tcher_user']
        content1 = request.POST.get('content1')
        question = request.POST.get('question')
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
            "id" : question,
        }
        file = {
            'image': image
        }
        response = requests.patch(url=urls, data=data, files=file, headers=headers)
        if response.status_code == 201:
            messages.success(request, {'msg': 'Question added successfully!','status': 'success'})
            return redirect('myQuestion')
        else:
            messages.error(request, {'msg': 'Something went wrong!','error': 'error'})
            return redirect('myQuestion')
    data = editQuestion(request,urls,id)
    return render(request, 'editWritingTestQuestion.html',context={'data':data})

def editReadingQuestion(request):
    return render(request, 'editReadingQuestion.html')

def editListeningQuestion(request,id):
    urls = f'{url}/teacher/listeningTests'
    if request.method == 'POST':
        audio = request.POST.get('audio_file')
        questionId = request.POST.get('questionId')
        headers = {
            "token": request.session['tcher_token']
        }
        data = {
            'questionId': questionId
        }
        file = {
            'question': audio
        }
        response = requests.patch(url=urls, data=data, files=file, headers=headers)
        if response.status_code == 201:
            messages.success(request, {'msg': 'Question added successfully!','status': 'success'})
            return redirect('myQuestion')
        else:
            messages.error(request, {'msg': 'Something went wrong!','error': 'error'})
            return redirect('myQuestion')
    data = editQuestion(request,urls,id)
    return render(request, 'editListeningTestQuestion.html',context={'data':data})

def editSpeakingQuestion (request,id):
    urls = f'{url}teacher/speakingTests'
    if request.method == 'POST':
        topic = request.POST.get('content')
        questionId = request.POST.get('question')
        urls = f'{url}teacher/speakingTests'
        headers = {
            "token": request.session['tcher_token']
        }
        data = {
            "question": topic,
            "questionId": questionId
        }
        response = requests.patch(url=urls, data=data, headers=headers)
        if response.status_code == 201:
            messages.success(request, {'msg': 'Question added successfully!', 'status': 'success'})
            return redirect('myQuestion')
        else:
            messages.error(request, {'msg': 'Something went wrong!', 'status': 'error'})
            return redirect('myQuestion')
    data = editQuestion(request,urls,id)
    return render(request, 'editSpeakingTestQuestion.html',context={'data':data})

########################
### delete Question ####
########################
    
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
        try:
            urls = f'{url}teacher/WritingQuestionsListView'
            headers={'token': request.session.get('tcher_token')}
            response = requests.get(url=urls,headers=headers)
            writingQuestions = response.json()
        except Exception as e:
            writingQuestions = {}
        
        try:
            urls = f'{url}teacher/ListeningQuestionListView'
            response = requests.get(url=urls,headers=headers)
            listeningQuestions = response.json()
        except Exception as e:
            listeningQuestions = {}
        
        try:
            urls = f'{url}teacher/ReadingQuestionListView'
            response = requests.get(url=urls,headers=headers)
            readingQuestions = response.json()
        except Exception as e: 
            readingQuestions = {}
        
        try:
            urls = f'{url}teacher/SpeakingQuestionListView'
            response = requests.get(url=urls,headers=headers)
            speakingQuestions = response.json()
        except Exception as e:
                speakingQuestions = {}
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

def editQuestion(request,urls,id):
    headers = {
        "token": request.session['tcher_token']
    }
    data = {
        "question": id,
    }
    response = requests.get(url=urls, data=data, headers=headers)
    try:
        jsonData = response.json()
        return jsonData
    except:
        return None    
    
###################################################