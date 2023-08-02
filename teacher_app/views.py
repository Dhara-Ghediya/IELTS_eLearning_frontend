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
            messages.success(request, {'msg': 'Question added successfully!'})
            return redirect('writingTest')
        else:
            messages.error(request, {'msg': 'Something went wrong!'})
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
        subQuestions = request.POST.getlist('ques')
        urls = f'{url}teacher/readingTests'
        headers = {
            "token": request.session['tcher_token']
        }
        data = {
            "teacher": tcher,
            "question": question,
            "subQuestion": subQuestions,
        }
        response = requests.post(url=urls, data=data, headers=headers)
        if response.status_code == 201:
            messages.success(request, {'msg': 'Question added successfully!'})
            return redirect('readingTest')
        else:
            messages.error(request, {'msg': 'Something went wrong!'})
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
        if response.status_code == 200:
            return render(request,'myQuestions.html', {'writingQuestions': response})
        else:
            return render(request,'myQuestions.html', {'response': response.json()})