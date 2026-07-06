from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Project, Category
from .forms import ContactMessageForm

def project_list(request):
    categories = Category.objects.all()
    selected_category = request.GET.get('category')
    if selected_category:
        projects = Project.objects.filter(category_slug=selected_category)
    else:
        projects = Project.objects.all()
    context = {
        'projects': projects,
        'categories': categories,
        'selected_category': selected_category,
    }
    return render(request, 'video/index.html', context)

def contact_view(request):
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Спасибо за обращение! Я свяжусь с вами в ближайшее время')
            return redirect('home')
    else:
        form = ContactMessageForm()
    return render(request, 'video/contact.html', {'form': form})