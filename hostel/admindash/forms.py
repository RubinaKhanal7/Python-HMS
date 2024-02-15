from django import forms
from .models import *
from django.core.validators import validate_integer


#Room
class RoomForm(forms.ModelForm):

    class Meta:
        model = Room
        fields = ['room_id','no_of_beds','floor_number','price','status',]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
            })

#BookRoom
class BookRoomForm(forms.ModelForm):

    class Meta:
        model = BookRoom
        fields = ['book_id','date','fullname','room_id','no_of_beds','floor_number','price', 'select_bed',]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date'].disabled = True
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
            })