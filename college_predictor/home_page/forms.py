from django import forms
from students.models import Student_Details
from django.contrib.auth.forms import UserCreationForm,password_validation,UserChangeForm
from django.contrib.auth.models import User

class StudentForm(forms.ModelForm):
    Username=forms.CharField(label='',widget=forms.TextInput(attrs={"id":"std_username","class":"std_username","disabled":"True"}))
    FirstName=forms.CharField(label='',widget=forms.TextInput(attrs={"id":"FirstName","placeholder":"Your First Name","maxlength":"50"}))
    LastName=forms.CharField(label='',widget=forms.TextInput(attrs={"id":"LastName","placeholder":"Your Last Name","maxlength":"50"}))
    City=forms.CharField(label='',widget=forms.TextInput(attrs={"id":"City","placeholder":"City Name","maxlength":"20"}))
    State=forms.CharField(label='',widget=forms.TextInput(attrs={"id":"State","placeholder":"State Name","maxlength":"20"}))
    Department=forms.CharField(label='',widget=forms.TextInput(attrs={"id":"Department","placeholder":"Department","maxlength":"20"}))
    Marks=forms.DecimalField(label='',widget=forms.TextInput(attrs={"type":"number","step":"0.01","min":"1","max":"100","id":"id_Marks","placeholder":"Enter your Marks"}))
    class Meta:
        model=Student_Details
        fields=[
            'image',
            'Username',
            'FirstName',
            'LastName',
            'City',
            'State',
            'Department',
            'Marks'
        ]

class EditForm(forms.ModelForm):
    class Meta:
        model=Student_Details
        fields=[
            'image',
            'FirstName',
            'LastName',
            'City',
            'State',
            'Department',
            'Marks',
            'Username',
        ]
    def clean(self):
        return self.cleaned_data