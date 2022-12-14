from django.shortcuts import render
from django.shortcuts import redirect, render
# Create your views here.

def home(request):
    return render(request, 'main.html',{})

def bitstream(request,id):
    context={
        'id':id,
    }
    return render(request, 'processing.html',context)  