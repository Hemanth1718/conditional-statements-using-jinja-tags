from django.shortcuts import render


# Create your views here.

def conditions(request):
    d={'a':11,'b':13, 'c':24}
    return render(request,'conditions.html',d)
