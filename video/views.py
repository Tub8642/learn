from django.shortcuts import render, redirect
from .models import Project
from .forms import ContactMessageForm

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'video/index.html', {'projects': projects})

def contact_view(request):
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thanks')
    else:
        form = ContactMessageForm()
    return render(request, 'video/contact.html', {'form': form})

def thanks_view(request):
    return render(request, 'video/thanks.html')