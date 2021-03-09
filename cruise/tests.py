from django.test import TestCase
from django.contrib.auth.models import User
from .models import TravelType, Trip, Questions
import datetime
from .forms import TripForm, TravelTypeForm, QuestionsForm
from django.urls import reverse_lazy, reverse
# Create your tests here.

class TravelTypeTest(TestCase):
    def setUp(self):
        self.type = TravelType(travelname = 'Yellow stone')

    def test_typestring(self):
        self.assertEqual(str(self.type), 'Yellow stone')

    def test_tablename(self):
        self.assertEqual(str(TravelType._meta.db_table), 'traveltype')  

class TripTest(TestCase):
    def setUp(self):
        self.type = TravelType(travelname = 'red tree')
        self.user = User(username='user1')
        self.trip = Trip(travelname='Yellow Stone Tour', traveltype=self.type, user=self.user, dateentered = datetime.date(2021,3,5), travelprice=979.877, reservedurl='http://wwww.yellowstone.html', questions="Havefun")

    def test_string(self):
        self.assertEqual(str(self.trip), 'Yellow Stone Tour') 

    def test_discount(self):
        disc = self.trip.travelprice * .05
        self.assertEqual(self.trip.discountPercent(), disc) 

class QuestionTest(TestCase):
    def setUp(self):
        self.type = TravelType(travelname = 'red tree')
        self.user = User(username='user1')
        self.trip = Trip(travelname='Yellow Stone Tour', traveltype=self.type, user=self.user, dateentered = datetime.date(2021,3,5), travelprice=979.877, reservedurl='http://wwww.yellowstone.html', questions="Havefun")     
        self.question = Questions(questiontitle="Where can I go", user=self.user, trip=self.trip, questiondate=datetime.date(2021,3,5), questiontext="Fun!")  


class NewTravelTypeForm(TestCase):
    def test_traveltypeform(self):
        data={
            'travelname' : 'Yellow stone',
            'travelquestions' : 'Is it hot?',
            'dateentered' : '2021-3-7',
            'questions' : 'Fun!' 
            } 
        
        form=TravelTypeForm(data)                   
        self.assertTrue(form.is_valid)


class NewTripForm(TestCase):
    def test_tripform(self):
        data={
            'travelname' : 'Yellow Stone', 
            'traveltype' : 'Trip', 
            'user' : 'Hijiri', 
            'dateentered' : '2021-3-7', 
            'travelprice' : '2099',
            'reservedurl' : 'http://yellow.com',
            'questions' : 'Have fun!'
            } 
        
        form=TripForm(data)                   
        self.assertTrue(form.is_valid)

class NewQuestionsForm(TestCase):
    def test_questionsform(self):
        data={
            'questiontitle' : 'Yellow stone is big',
            'user' : 'Hijiri', 
            'trip' : 'Yellow stone', 
            'questiondate' : '2021-3-7', 
            'questiontext' : 'Fun!'
            } 
        
        form=QuestionsForm(data)                   
        self.assertTrue(form.is_valid)


class New_Trip_Authentication_Test(TestCase):
    def setUp(self):
        self.test_user= User.objects.create_user(username='testuser1', password='P@ssw0rd1')
        self.type=TravelType.objects.create(travelname = 'Statue of liberty', travelquestions = 'fun', dateentered = datetime.date(2021,1,29), questions='Super')
        self.trip=Trip.objects.create(travelname='Yellow Stone Tour', traveltype=self.type, user=self.test_user, dateentered = datetime.date(2021,1,29), travelprice=979.877, reservedurl='http://wwww.yellowstone.html', questions="Havefun")
        

    def test_redirect_if_not_logged_in(self):
        response=self.client.get(reverse('newtrip'))
        self.assertRedirects(response, '/accounts/login/?next=/cruise/newtrip/') 


class New_TravelType_Authentication_Test(TestCase):
    def setUp(self):
        self.test_user=User.objects.create_user(username='testuser1', password='P@ssw0rd1')
        self.type=TravelType.objects.create(travelname = 'Statue of liberty', travelquestions = 'fun', dateentered = datetime.date(2021,1,29), questions='Super')
        self.trip=Trip.objects.create(travelname='Yellow Stone Tour', traveltype=self.type, user=self.test_user, dateentered = datetime.date(2021,1,29), travelprice=979.877, reservedurl='http://wwww.yellowstone.html', questions="Havefun")
        # self.traveltype=TravelType.objects.create(questions='Fun!')

    def test_redirect_if_not_logged_in(self):
        response=self.client.get(reverse('newtraveltype'))
        self.assertRedirects(response, '/accounts/login/?next=/cruise/newtraveltype/')   
    


class New_Questions_Authentication_Test(TestCase):
    def setUp(self):
        self.test_user=User.objects.create_user(username='testuser1', password='P@ssw0rd1')
        self.type=TravelType.objects.create(travelname = 'Statue of liberty', travelquestions = 'fun', dateentered = datetime.date(2021,1,29), questions='Super')
        self.trip=Trip.objects.create(travelname='Yellow Stone Tour', traveltype=self.type, user=self.test_user, dateentered = datetime.date(2021,3,5), travelprice=979.877, reservedurl='http://wwww.yellowstone.html', questions="Havefun")
        self.question=Questions.objects.create(questiontitle="Where can I go", user=self.test_user, trip=self.trip, questiondate=datetime.date(2021,3,5), questiontext="Fun!")  


    def test_redirect_if_not_logged_in(self):
        response=self.client.get(reverse('newquestions'))
        self.assertRedirects(response, '/accounts/login/?next=/cruise/newquestions/')     

