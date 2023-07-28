from django.shortcuts import render, redirect
from IELTS_eLearning_frontend.localsettings import url
from django.contrib import messages
import requests

def writingTest(request):
    if request.method == 'POST':
        tcher = request.session['tcher_user']
        content = request.POST.get('content')
        images = request.FILES.get('images')
        urls = f'{url}teacher/writingTests'
        data = {
            "teacher": tcher,
            "content": content,
            # "images": images,
        }
        file = {
            'images': images
        }
        response = requests.post(url=urls, data=data, files=file)
        if response.status_code == 201:
            messages.success(request, {'msg': 'Question added successfully!'})
            return redirect('writingTest')
        else:
            messages.error(request, {'msg': 'Something went wrong!'})
            return redirect('writingTest')
    return render(request, 'writingTest.html')

def listeningTest(request):
    if request.method == 'POST':
        tcher = request.session['tcher_user']
        audio = request.FILES.get('audio_file')
        urls = f'{url}teacher/listeningTests'
        data = {
            "teacher": tcher,
            # "question": audio,
        }
        file = {
            'question': audio
        }
        response = requests.post(url=urls, data=data, files=file)
        if response.status_code == 201:
            messages.success(request, {'msg': 'Question added successfully!'})
            return redirect('listeningTest')
        else:
            messages.error(request, {'msg': 'Something went wrong!'})
            return redirect('listeningTest')
    return render(request, 'listeningTest.html')

def speakingTest(request):
    if request.method == 'POST':
        tcher = request.session['tcher_user']
        topic = request.POST.get('content')
        urls = f'{url}teacher/speakingTests'
        data = {
            "teacher": tcher,
            "question": topic,
        }
        response = requests.post(url=urls, data=data)
        if response.status_code == 201:
            messages.success(request, {'msg': 'Question added successfully!'})
            return redirect('speakingTest')
        else:
            messages.error(request, {'msg': 'Something went wrong!'})
            return redirect('speakingTest')
    return render(request,'speakingTest.html')

def readingTest(request):
    if request.method == 'POST':
        tcher = request.session['tcher_user']
        question = request.POST.get('content')
        que1 = request.POST.get('first_que')
        que2 = request.POST.get('second_que')
        que3 = request.POST.get('third_que')
        que4 = request.POST.get('fourth_que')
        que5 = request.POST.get('fifth_que')
        urls = f'{url}teacher/readingTests'
        data = {
            "teacher": tcher,
            "question": question,
            "question1": que1,
            "question2": que2,
            "question3": que3,
            "question4": que4,
            "question5": que5,
        }
        response = requests.post(url=urls, data=data)
        print("Response", response, response.status_code)
        if response.status_code == 201:
            print("Successfully created", response.status_code)
            messages.success(request, {'msg': 'Question added successfully!'})
            return redirect('readingTest')
        else:
            print("Error creating")
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