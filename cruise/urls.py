from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('traveltypes/', views.traveltypes, name='traveltypes'),
    path('trips/', views.trips, name='trips'),
    path('questions/', views.questions, name='questions'),
    path('traveltypeDetail/<int:id>', views.traveltypeDetail, name='detail1'),
    path('tripDetail/<int:id>', views.tripDetail, name='detail'),
    path('questionDetail/<int:id>', views.questionDetail, name='detail2'),
    path('newtraveltype/', views.newTravelType, name='newtraveltype'),
    path('newtrip/', views.newTrip, name='newtrip'),
    path('newquestions/', views.newQuestions, name='newquestions'),
    path('loginmessage/', views.loginmessage, name='loginmessage'),
    path('logoutmessage/', views.logoutmessage, name='logoutmessage'),

]