from django.shortcuts import render, get_object_or_404, redirect
from flow.models import Flow, Notification
from django.http import Http404

def index(request):

    return render(request, 'flow/index.html')


def showFlow(request):
    pass

def addFlow(request):
    pass

def editFlow(request):
    pass

def showNotif(request):
    pass

def addNotif(request):
    pass

def editNotif(request):
    pass
