from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def show_list(request):
    return render(request,'list.html')


# Create your views here.
