from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class TravelType(models.Model):
    travelname=models.CharField(max_length=255)
    travelquestions=models.TextField(null=True, blank=True)
    dateentered=models.DateField()
    questions=models.TextField()



    def __str__(self):
        return self.travelname

    class Meta:
        db_table='traveltype'

class Trip(models.Model):
    travelname=models.CharField(max_length=255)
    traveltype=models.ForeignKey(TravelType, on_delete=models.DO_NOTHING)
    user=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    dateentered=models.DateField()
    travelprice=models.DecimalField(max_digits=7, decimal_places=2)
    reservedurl=models.URLField()
    questions=models.TextField()

    def discountPercent(self):
        self.discount = self.travelprice * .05
        return self.discount

    def discountPrice(self):
        self.discountedPrice = self.price - self.discount     

    def __str__(self):
        return self.travelname

    class Meta:
        db_table='trip'

class Questions(models.Model):
    questiontitle=models.CharField(max_length=255)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    trip=models.ForeignKey(Trip, related_name='+', on_delete=models.CASCADE)
    questiondate=models.DateField()
    questiontext=models.TextField()

    def __str__(self):
        return self.questiontitle

    class Meta:
        db_table='questions'    