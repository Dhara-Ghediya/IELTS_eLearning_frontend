from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('writingTest', views.teacherWritingTest, name="writingTest"),
    path('listeningTest', views.teacherListeningTest, name="listeningTest"),
    path('speakingTest', views.teacherSpeakingTest, name="speakingTest"),
    path('readingTest', views.teacherReadingTest, name="readingTest"),
    path('myQuestion',views.myQuestions, name="myQuestion"),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)