from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from flow.models import Flow, Notification, OriginConnection, DestinyConnection
from flow.forms import FlowForm, NotificationForm, NotificationFormEdit
from django.http import Http404
from django.contrib.auth.decorators import login_required

def index(request):
    all_flows = Flow.objects.filter(owner = request.user)
    # all_flows = Flow.objects.all()
    context = {
        "flows" : all_flows
    }
    return render(request, 'index.html', context)


def showFlow(request, process_id):

    single_flow = get_object_or_404(Flow.objects.filter(id=process_id, owner = request.user))

    context = {}

    notifications = (Notification.objects.filter(flow=single_flow.id))

    if notifications:
        context = {
            "flow" : single_flow,
            "notification" : notifications
        }
        return render(request, 'flow.html', context)

    context = {
            "flow" : single_flow,
            "notification" : []
        }
    
    return render(request, 'flow.html', context)

def addFlow(request):
    form_action = reverse('flow:addFlow')
    if request.method == 'POST':
        form = FlowForm(request.POST)
        context = {'name': "Flow", 'form': form, 'form_action': form_action}

        if form.is_valid():
            new_flow = form.save(commit=False)
            new_flow.owner = request.user
            new_flow.save()
            
            return redirect('flow:index')
        
        return render(request, 'create.html', context)
    
    context = {'name': "Flow", 'form': FlowForm()}
    return render(request, 'create.html', context)

def editFlow(request, process_id):
    flow = get_object_or_404(Flow, pk=process_id, owner=request.user)
    form_action = reverse('flow:editFlow', args=(process_id,))
    if request.method == 'POST':
        form = FlowForm(request.POST, instance=flow)

        context = {'name': "Flow", 'form': form, 'form_action': form_action}

        if form.is_valid():
            edit_flow = form.save()
            return redirect('flow:index')
            # return redirect('flow:editFlow', process_id=edit_flow.id)
        
        return render(request, 'create.html', context)
    
    context = {
        'name': "Flow",
        'form': FlowForm(instance=flow),
        'form_action': form_action
    }

    return render(request, 'create.html', context)

def showNotif(request, notification_id):
    single_notif = get_object_or_404(Notification.objects.filter(id=notification_id))
    singleOrCon = OriginConnection.objects.filter(notification=single_notif).first()
    singleDesCon = DestinyConnection.objects.filter(notification=single_notif).first()

    context = {
        "origen_con": singleOrCon,       
        "destiny_con": singleDesCon,
    }
    
    return render(request, 'transaction.html', context)

def addNotif(request):
    form_action = reverse('flow:addNotif')
    if request.method == 'POST':
        form = NotificationForm(request.POST)
        context = {'name': "Transaction", 'form': form, 'form_action': form_action}

        if form.is_valid():
            new_notification = form.save(commit=False)
            new_notification.owner = request.user
            new_notification.save()
            
            return redirect('flow:index', transaction_id=new_notification.transaction_id)
        
        return render(request, 'create.html', context)
    
    context = {'name': "Transaction", 'form': NotificationForm()}
    return render(request, 'create.html', context)

def editNotif(request, transaction_id):
    notif = get_object_or_404(Notification, pk=transaction_id, owner=request.user)
    form_action = reverse('flow:editNotif', args=(transaction_id,))
    if request.method == 'POST':
        form = NotificationFormEdit(request.POST, instance=notif)

        context = {'name': "Notification", 'form': form, 'form_action': form_action}

        if form.is_valid():
            edit_notif = form.save()
            single_flow = Flow.objects.filter(pk=notif.flow.id).first()
            return redirect('flow:showFlow', process_id=single_flow.id)
        
        return render(request, 'create.html', context)
    
    context = {
        'name': "Notification",
        'form': NotificationFormEdit(instance=notif),
        'form_action': form_action
    }

    return render(request, 'create.html', context)


def originCon(request):
    pass

def destinyCon(request):
    pass
