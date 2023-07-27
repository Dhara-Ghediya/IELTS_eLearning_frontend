from django.urls import path
from . import views

urlpatterns = [
    path('writingTest', views.writingTest, name="writingTest"),
    path('listeningTest', views.listeningTest, name="listeningTest"),
    path('speakingTest', views.speakingTest, name="speakingTest"),
    path('readingTest', views.readingTest, name="readingTest"),
]