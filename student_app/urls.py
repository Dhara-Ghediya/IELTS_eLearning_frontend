from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('profile', views.profile, name='profile'),
    path('examLibrary', views.examLibrary, name='examLibrary'),
    path('writing-test', views.writingTest, name='writing_test'),
    path('listening-test', views.listeningTest, name='listening_test'),
    path('speaking-test', views.speakingTest, name='speaking_test'),
    path('reading-test', views.readingTest, name='reading_test'),

    path('courses', views.courses, name="courses"),
    path('about', views.about, name="about"),
    path('contact', views.contact, name="contact"),
    path('team', views.team, name="team"),
    path('testimonial', views.testimonial, name="testimonial"),
    path('404', views.four04, name="404"),
]