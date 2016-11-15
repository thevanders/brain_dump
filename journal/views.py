from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.core.urlresolvers import reverse
from .models import *
from .forms import *

today = datetime.today().strftime("%Y-%m-%d")

images = DailyImage.objects.get(date=today)
if images.location:
    name = images.name + ", " + images.location
else:
    name = images.name


# Create your views here.
def IndexView(request):
    journal_entries = JournalEntry.objects.order_by('-pk')
    template = loader.get_template('journal/index.html')
    context = {
        'journal_entries': journal_entries,
        'images': images,
        'name': name,
        'today': today,
    }
    return HttpResponse(template.render(context, request))

def EntryView(request):
    if request.method == 'POST':
        form = JournalEntryForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('journal:index_view'))
    else:
        form = JournalEntryForm()
    return render(request, 'journal/add_entry.html', {
        'form': form,
        'images': images,
        'today': today,
    })
