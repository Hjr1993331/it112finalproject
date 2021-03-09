from django.shortcuts import render, get_object_or_404 
from .models import TravelType, Trip, Questions
from .forms import TripForm, TravelTypeForm, QuestionsForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    return render(request, 'cruise/index.html')

@login_required
def traveltypes(request):
    traveltype_list=TravelType.objects.all()
    return render(request, 'cruise/traveltypes.html', {'traveltype_list': traveltype_list}) 

@login_required
def trips(request):
    trip_list=Trip.objects.all()
    return render(request, 'cruise/trips.html', {'trip_list': trip_list})    

@login_required
def questions(request):
    question_list=Questions.objects.all()
    return render(request, 'cruise/questions.html', {'question_list': question_list})   

@login_required
def traveltypeDetail(request, id):
    traveltype=get_object_or_404(TravelType, pk=id)
    return render(request, 'cruise/traveltypedetail.html', {'traveltype' : traveltype}) 

@login_required
def tripDetail(request, id):
    trip=get_object_or_404(Trip, pk=id)
    return render(request, 'cruise/tripdetail.html', {'trip' : trip})     

@login_required
def questionDetail(request, id):
    question=get_object_or_404(Questions, pk=id)
    return render(request, 'cruise/questiondetail.html', {'question' : question})     


@login_required
def newTravelType(request):
    form=TravelTypeForm

    if request.method=='POST':
        form=TravelTypeForm(request.POST)
        if form.is_valid():
            post=form.save(commit = True)
            post.save()
            form=TravelTypeForm()
    else:
        form=TravelTypeForm()
    return render(request, 'cruise/newtraveltype.html', {'form': form})  


@login_required
def newTrip(request):
    form=TripForm

    if request.method=='POST':
        form=TripForm(request.POST)
        if form.is_valid():
            post=form.save(commit = True)
            post.save()
            form=TripForm()
    else:
        form=TripForm()
    return render(request, 'cruise/newtrip.html', {'form': form})            


@login_required
def newQuestions(request):
    form=QuestionsForm

    if request.method=='POST':
        form=QuestionsForm(request.POST)
        if form.is_valid():
            post=form.save(commit = True)
            post.save()
            form=QuestionsForm()
    else:
        form=QuestionsForm()
    return render(request, 'cruise/newquestions.html', {'form': form})  


def loginmessage(request):
    return render(request, 'cruise/loginmessage.html')

def logoutmessage(request):
    return render(request, 'cruise/logoutmessage.html')        