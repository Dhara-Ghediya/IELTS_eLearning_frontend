from django.urls import path
from . import views

urlpatterns = [
    path('writingTest', views.teacherWritingTest, name="writingTest"),
    path('listeningTest', views.teacherListeningTest, name="listeningTest"),
    path('speakingTest', views.teacherSpeakingTest, name="speakingTest"),
    path('readingTest', views.teacherReadingTest, name="readingTest"),
    path('myQuestion',views.myQuestions, name="myQuestion"),
]