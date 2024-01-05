from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from flow.models import Flow, Notification
from flow.forms import FlowForm, NotificationForm
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

    context = {
        "flow" : single_flow
    }
    
    return render(request, 'flow.html', context)

def addFlow(request):
    form_action = reverse('flow:addFlow')
    if request.method == 'POST':
        form = FlowForm(request.POST)
        context = {'form': form, 'form_action': form_action}

        if form.is_valid():
            new_flow = form.save(commit=False)
            new_flow.owner = request.user
            new_flow.save()
            
            return redirect('flow:index')
        
        return render(request, 'create.html', context)
    
    context = {'form': FlowForm()}
    return render(request, 'create.html', context)

def editFlow(request, process_id):
    flow = get_object_or_404(Flow, pk=process_id, owner=request.user)
    form_action = reverse('flow:editFlow', args=(process_id,))
    if request.method == 'POST':
        form = FlowForm(request.POST, instance=flow)

        context = {'form': form, 'form_action': form_action}

        if form.is_valid():
            edit_flow = form.save()
            return redirect('flow:editFlow', process_id=edit_flow.id)
        
        return render(request, 'create.html', context)
    
    context = {
        'form': FlowForm(instance=flow),
        'form_action': form_action
    }

    return render(request, 'create.html', context)

def showNotif(request):
    pass

def addNotif(request):
    form_action = reverse('flow:create')
    if request.method == 'POST':
        form = NotificationForm(request.POST)
        context = {'form': form, 'form_action': form_action}

        if form.is_valid():
            new_notif = form.save(commit=False)
            new_notif.owner = request.user
            new_notif.save()
            
            return redirect('flow:index', transaction_id = new_notif.transaction_id)
        
        return render(request, 'flow/create.html', context)

def editNotif(request):
    pass
