from django.shortcuts import render, get_object_or_404, redirect
from .models import Entry

# Create your views here.

def guestBook(request):
    return render(request, 'guestBook.html')

def addMessage(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        title = request.POST.get('title')
        message = request.POST.get('message')
        if name and title and message:
            Entry.objects.create(name=name, title=title, message=message)
            return render(request, 'add.html', {'success': True})
        
        return render(request, 'add.html', {'error': "All fields are required!"})
    
    return render(request, 'add.html')

def viewEntries(request):
    entries = Entry.objects.all()
    return render(request, 'entries.html', {'entries': entries})

def viewMessage(request, message_id):
    entry = get_object_or_404(Entry, id=message_id)
    return render(request, 'message.html', {'entry': entry})


