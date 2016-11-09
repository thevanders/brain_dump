from django.forms import ModelForm, Textarea
from django.utils.translation import ugettext_lazy as _
from .models import *

class JournalEntryForm(ModelForm):
    class Meta:
        model = JournalEntry
        exclude = ['date', 'image']
