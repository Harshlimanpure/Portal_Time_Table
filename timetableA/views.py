from django.shortcuts import render , redirect
from .models import *
from .forms import * 
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def sem1(request):
    timetablesem1 = Sem1.objects.all()
    return render(request, 'sem1.html',{'timetablesem1':timetablesem1})

@login_required
def sem2(request):
    timetablesem2 = Sem2.objects.all()
    return render(request, 'sem2.html',{'timetablesem2':timetablesem2})

@login_required
def sem3(request):
    timetablesem3 = Sem3.objects.all()
    return render(request, 'sem3.html',{'timetablesem3':timetablesem3})

@login_required
def sem4(request):
    timetablesem4 = Sem4.objects.all()
    return render(request, 'sem4.html',{'timetablesem4':timetablesem4})

@login_required
def sem5(request):
    timetablesem5 = Sem5.objects.all()
    return render(request, 'sem5.html',{'timetablesem5':timetablesem5})


@login_required
def sem6(request):
    timetablesem6 = Sem6.objects.all()
    return render(request, 'sem6.html',{'timetablesem6':timetablesem6})

@login_required
def sem7(request):
    timetablesem7 = Sem7.objects.all()
    return render(request, 'sem7.html',{'timetablesem7':timetablesem7})

@login_required
def sem8(request):
    timetablesem8 = Sem8.objects.all()
    return render(request, 'sem8.html',{'timetablesem8':timetablesem8})

# def register(request):
#     if request.method == 'POST':
#         form = RegForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')
#     else:
#         form = RegForm()
#     return render(request, 'reg.html',{'form':form})