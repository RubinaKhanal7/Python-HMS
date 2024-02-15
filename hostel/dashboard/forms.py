from django import forms
from .models import *
from django.core.validators import validate_integer

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
