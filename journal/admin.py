from django.contrib import admin
from journal.models import *

# Register your models here.
myModels = [JournalEntry]
admin.site.register(myModels)
