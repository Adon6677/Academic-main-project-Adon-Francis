from django import forms
from django.db.models import fields 
from .models import *

class RegisterForm(forms.ModelForm):
    class Meta:
        model= Stadium_Profile
        exclude= ('user','created','updated')
        
class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        exclude = ('user','created','updated', 'remaining_seats')

class GameCategoryForm(forms.ModelForm):
    class Meta:
        model = GameCategory
        fields = ['name', 'image']
        
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        exclude = ('user','created','updated')
        
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact 
        exclude = ('created','contact_status')  
        
class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        exclude = ('user','created','updated')
        