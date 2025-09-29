from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .forms import eventForm, prayerRequestForm
from .models import userModel

@login_required
def dashboardView(request):
    return render(request, 'core/dashboard.html')


@staff_member_required
def createEventView(request):
    
    if request.method == 'POST':
        form = eventForm(request.POST)

        if form.is_valid():
            event = form.save(commit=False)
            event.created_by = request.user
            event.save()
            return redirect('core:dashboard')
    else:
         form = eventForm()
    return render(request, 'core/createEvents.html', {'form': form})

@login_required
def createPrayerRequestView(request):
    if request.method == 'POST':
        form = prayerRequestForm(request.POST)

        if form.is_valid():
            prayerRequest = form.save(commit=False)
            prayerRequest.created_by = request.user
            prayerRequest.save()
            return redirect('core:dashboard')
    else:
         form = prayerRequestForm()

    return render(request, 'core/createPrayerRequests.html', {'form': form})

@staff_member_required
def memberListView(request):
    users = userModel.objects.all()
    return render(request, 'core/memberList.html', {'users': users})
