from django.shortcuts import render
from students.models import Student_Details
from .models import College_Details

def predict_clg(request):
    stream,state='',''
    if request.method=='POST':
        stream=request.POST['stream']
        state=request.POST['state']
        print(stream,state)  
    context={
        'stream':stream,
        'state':state,
        'data':College_Details.objects.all(),
        'std':Student_Details.objects.get(Username=request.user.id)
    }
    return render(request,'colleges/predict.html',context)
