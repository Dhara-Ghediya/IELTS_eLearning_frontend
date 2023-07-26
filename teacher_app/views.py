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
            messages.success(request, 'Question added successfully!')
            return redirect('writingTest')
        else:
            messages.error(request, 'Something went wrong!')
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
        print("response..", response.status_code)
        if response.status_code == 201:
            messages.success(request, 'Question added successfully!')
            return redirect('listeningTest')
        else:
            messages.error(request, 'Something went wrong!')
            return redirect('listeningTest')
    return render(request, 'listeningTest.html')