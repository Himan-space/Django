from django import forms
from students.models import Student_Details
from .models import College_Details
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class predict(forms.ModelForm):
    select_stream=(("Computer","Computer"),("Information Technology","Information Technology"),("Mechanical","Mechanical"),("Electronics","Electronics"),("Civil","Civil"))
    Stream=forms.ChoiceField(label='Select your stream',widget=forms.Select(attrs={},choice=select_stream))
    select_state=(("Maharastra","Maharastra"),("Karnataka","Karnataka"),("Telangana","Telangana"))
    State=forms.ChoiceField(label='Select your stream',widget=forms.Select(attrs={},choice=select_state))
    def clean(self):
        return self.cleaned_data