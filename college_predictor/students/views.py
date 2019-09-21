from django.shortcuts import render,redirect
from .models import Student_Details
from home_page.forms import EditForm
from django.http import Http404


def student_profile(request):
    data=Student_Details.objects.get(Username=request.user.id)
    context={
        'data':data
    }
    return render(request,'students/std_details.html',context)

def edit_profile(request):
    instance = Student_Details.objects.get(Username=request.user.id)
    form = EditForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect(student_profile)
    else:
        print('error')
    return render(request, 'students/edit.html', {'form': form})

