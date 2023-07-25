from django.shortcuts import render, redirect
from IELTS_eLearning_frontend.localsettings import url
from django.contrib import messages
import requests

# Create your views here.
# def home(request):
#     return render(request, 'index.html')


# def login(request):
#     return render(request, 'login.html')

# def logout(request):
#     return render(request, 'logout.html')

# def profile(request):
#     return render(request, 'profile.html')

def writingTest(request):
    if request.method == 'POST':
        tcher = request.session['tcher_user']
        content = request.POST.get('content')
        images = request.POST.get('images')
        marks = request.POST.get('marks')
        urls = f'{url}teacher/writing-tests'
        # urls="http://127.0.0.1:8000/teacher/listning-tests"
        print("url:",urls)
        data = {
            "teacher": tcher,
            "content": content,
            "images": images,
            "questionMarks": marks,
        }
        response = requests.post(url=urls, json=data)
        print(response.status_code, "yyiyi")
        if response.status_code == 201:
            messages.success(request, 'Question added successfully!')
            return redirect('writingTest')
        else:
            messages.error(request, 'Something went wrong!')
            return redirect('writingTest')
    return render(request, 'writingTest.html')

# def about(request):
#     return render(request, 'about.html')

# def contact(request):
#     return render(request, 'contact.html')

# def team (request):
#     return render(request, 'team.html')

# def testimonial(request):
#     return render(request, 'testimonial.html')

# def four04(request):
#     return render(request, '404.html')