from django.shortcuts import render, get_object_or_404, redirect
from flow.models import Flow, Notification
from django.http import Http404

def index(request):
    # all_flows = Flow.objects.filter(owner = request.user)
    all_flows = Flow.objects.all()
    context = {
        "flows" : all_flows
    }
    return render(request, 'index.html', context)


def showFlow(request, process_id):

    single_flow = get_object_or_404(Flow.objects.filter(process_id=process_id, owner = request.user))

    context = {
        "flow" : single_flow
    }
    
    return render(request, 'flow.html', context)

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
