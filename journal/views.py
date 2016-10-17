from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import *
from .forms import *

# Create your views here.
def IndexView(request):
    journal_entries = JournalEntry.objects.all()
    template = loader.get_template('journal/index.html')
    context = {
        'journal_entries': journal_entries
    }
    return HttpResponse(template.render(context, request))

def EntryView(request):
    if request.method == 'GET':
        form = JournalEntryForm()
    else:
        # A POST request: Handle Form Upload
        # Bind data from request.POST into a PostForm
        form = JournalEntryForm(request.POST)
        # If data is valid, proceeds to create a new post and redirect the user
        #if form.is_valid():
        #    content = form.cleaned_data['content']
        #    created_at = form.cleaned_data['created_at']
        #    post = m.Post.objects.create(content=content, created_at=created_at)
        #    return HttpResponseRedirect(reverse('post_detail', kwargs={'post_id': post.id}))

    return render(request, 'journal/entry.html', {
        'form': form,
    })
