from distutils.command.upload import upload
from unicodedata import category
from django.db import models
import datetime
from django.core.exceptions import ValidationError
from unicodedata import category
from django.core.validators import  MinValueValidator
# Create your models here.



class Room(models.Model):
    room_id = models.IntegerField()
    no_of_beds = models.IntegerField()
    floor_number = models.IntegerField()
    price = models.IntegerField()
    status = models.CharField(max_length=255)


    class Meta:
        verbose_name = "Room"
        verbose_name_plural = "Rooms"
        ordering = ('room_id',)

    
    def __str__(self):
        return self.room_id

class BookRoom(models.Model): 
    book_id = models.IntegerField(unique=True)
    date = models.DateField(default=datetime.date.today())
    fullname = models.CharField(max_length=255)
    room_id = models.IntegerField()
    no_of_beds = models.IntegerField(validators=[MinValueValidator(1)])
    floor_number = models.IntegerField(validators=[MinValueValidator(1)])
    price = models.IntegerField(validators=[MinValueValidator(1)])
    select_bed = models.IntegerField(validators=[MinValueValidator(1)])

    class Meta:
        verbose_name = "BookRoom"
        verbose_name_plural = "BookRooms"
        ordering = ('book_id',)
        
    def __str__(self):
        return self.book_id
